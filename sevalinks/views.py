from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import logout
import forms
import models
import configs
import utils
from django.core import validators
import lepl.apps.rfc3696 as rfc
from passlib.hash import pbkdf2_sha256 as hashPass
import datetime
import smtp_email
import classifieds.settings as settings

# Create your views here.
def home(request):
    if utils.authenticate_session(request):
        return redirect("/seva/userhome/")
    else:
        return render(request, "sevalinks/home.html")

def change_image_render(request):
    if utils.authenticate_session(request):
        return render(request, "sevalinks/changeimage.html")
    else:
        return redirect("/404/")

def user_login(request):
    contextDict = {}
    validation_error = "Invalid email or password."
    if request.method == "POST":
        print request.POST
        loginForm = forms.UserLoginForm(request.POST)
        print loginForm
        if loginForm.is_valid():
            loginInfo = loginForm.cleaned_data
            contextDict = loginInfo
            if utils.authenticate_user(loginInfo["email"], loginInfo["password"]):
                userInfo = utils.get_user_as_dict(loginInfo["email"])
                request.session["user_id"] = userInfo["user_id"]
                return redirect("/seva/userhome/")
    else:
        return render(request, "sevalinks/login.html")

    contextDict['validation_error'] = validation_error
    return render(request, "sevalinks/login.html", contextDict)

def user_register(request):
    contextDict = {}
    if request.method == "POST":
        print request.POST
        regForm = forms.UserRegisterForm(request.POST)
        if regForm.is_valid():
            contextDict = regForm.cleaned_data
            regStatus = utils.validate_user(contextDict)
            if regStatus == 1:
                print "====saving user===="
                if settings.REG_EMAIL_CONFIRM:
                    utils.save_user(contextDict)
                    confirmId = utils.create_random_identifier()
                    user = utils.get_user_as_dict(contextDict["email"])
                    utils.add_confirmation_id(user["user_id"], confirmId)
                    #sendemail(contextDict["email"], confirmId)
                    smtp_email.send_register_confirm_email(confirmId, user["first_name"], contextDict["email"])
                else:
                    utils.save_user_temp(contextDict)
                return redirect("/seva/confirmrequest/")
            else:
                contextDict['validation_error'] = regStatus
        else:
            contextDict = request.POST.dict()
            contextDict['validation_error'] = "Empty field or invalid input"
    else:
        regForm = forms.UserRegisterForm()

    contextDict['formtype'] = "register"
    return render(request, "sevalinks/user_registeration.html", contextDict)

def user_account(request):
    userId = request.session["user_id"]
    contextDict = utils.get_user_with_id(userId)
    contextDict.update(utils.get_user_location_with_id(userId))
    contextDict.update(utils.get_user_profession_with_id(userId))
    contextDict.update(utils.get_user_image_as_dict(userId))
    return render(request, "sevalinks/user_account.html", contextDict)

def confirm_render(request):
    return render(request, "sevalinks/user_confirmation.html")

def confirm_success(request):
    confirmId = request.GET.get("id", "")
    if confirmId != "":
        userConfirm = utils.get_user_from_confirmation(confirmId)
        if userConfirm:
            print userConfirm, userConfirm.user_id_id
            userData = {"user_id": str(userConfirm.user_id_id), "user_active": True, "last_login": datetime.datetime.now()}
            utils.update_user(userData, userFields=["user_active", "last_login"])
            userConfirm.user_confirmed = True
            userConfirm.confirmation_completed = datetime.datetime.now()
            userConfirm.save()
            request.session["user_id"] = str(userConfirm.user_id_id)
            return render(request, "sevalinks/user_confirmed.html")

    return redirect("/404/")


def edit_profile_render(request):
    contextDict = {}
    userId = request.session.get("user_id")
    if not userId:
        logout(request)
        return redirect("/seva/login/")
    contextDict = utils.get_user_with_id(userId)
    contextDict.update(utils.get_user_image_as_dict(userId))
    return render(request, "sevalinks/edit_profile.html", contextDict)

def edit_profile(request):
    contextDict = {}
    userId = request.session.get("user_id")
    if not userId:
        logout(request)
        return redirect("/seva/login/")
    if request.method == "POST":
        editInfo = request.POST.dict()
        if set(configs.USER_EDIT_FIELDS).issubset(editInfo):
            editStatus = utils.validate_edit_user(editInfo)
            if editStatus == 1:
                print "====updating user===="
                editInfo["user_id"] = userId
                utils.update_user(editInfo)
                return redirect("/seva/myaccount/")
            else:
                contextDict = editInfo
                contextDict['validation_error'] = editStatus
                return render(request, "sevalinks/edit_profile.html", contextDict)
    contextDict = utils.get_user_with_id(userId)
    contextDict.update(utils.get_user_image_as_dict(userId))
    return render(request, "sevalinks/edit_profile.html", contextDict)

def reset_password(request):
    contextDict = {}
    resetId = request.GET.get("id", "")
    if resetId == "":
        return redirect("/404/")
    else:
        userReset = utils.get_user_from_resetpassword(resetId)
        if not userReset:
            return redirect("/404/")
    if request.method == "POST":
        editInfo = request.POST.dict()
        if editInfo["password"] != editInfo["confirm_password"]:
            contextDict['validation_error'] = "Passwords do not match"
        else:
            userData = {"user_id": str(userReset.user_id), "password": hashPass.hash(editInfo["password"])}
            utils.update_user(userData, userFields=["password"])
            userReset.password_reset = True
            userReset.reset_completed = datetime.datetime.now()
            userReset.save()
            contextDict["reset_success"] = "success"
            logout(request)
    return render(request, "sevalinks/reset_password.html", contextDict)

def change_password(request):
    contextDict = {}
    userId = request.session.get("user_id", "")
    if userId == "":
        return redirect("/404/")

    if request.method == "POST":
        editInfo = request.POST.dict()
        if editInfo["password"] != editInfo["confirm_password"]:
            contextDict['validation_error'] = "Passwords do not match"
        else:
            userData = {"user_id": userId, "password": hashPass.hash(editInfo["password"])}
            utils.update_user(userData, userFields=["password"])
            contextDict["reset_success"] = "success"
    return render(request, "sevalinks/change_password.html", contextDict)

def reset_password_request(request):
    contextDict = {}
    contextDict["reset_request_success"] = "success"
    return render(request, "sevalinks/forgot_password.html", contextDict)

def forgot_password(request):
    contextDict = {}
    if request.method == "POST":
        editInfo = request.POST.dict()
        contextDict["email"] = editInfo["email"]
        emailStatus = utils.validate_email(editInfo["email"])
        if emailStatus == 1:
            resetId = utils.create_random_identifier()
            user = utils.get_user_as_dict(editInfo["email"])
            utils.add_reset_password_id(user["user_id"], resetId)
            smtp_email.send_reset_email(resetId, user["first_name"], editInfo["email"])
            #sendemail(editInfo["email"], resetId)
            return redirect("/seva/resetrequestsuccess/")
        else:
            contextDict['validation_error'] = emailStatus
    return render(request, "sevalinks/forgot_password.html", contextDict)

def user_logout(request):
    logout(request)
    return redirect("/")

def user_subscriptions(request):
    return render(request, "sevalinks/user_services.html")

def add_services(request):
    return render(request, "sevalinks/add_services.html")

def sevalinks_404(request):
    return render(request, "sevalinks/sevalinks_404.html")

def sevalinks_500(request):
    return render(request, "sevalinks/sevalinks_500.html")
