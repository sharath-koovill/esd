from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import logout
from django.http import JsonResponse
import forms
import models
import configs
import utils, search_handler
from django.core import validators
import lepl.apps.rfc3696 as rfc
from passlib.hash import pbkdf2_sha256 as hashPass
import datetime
import image_handler
from contacts.manager import ContactsManager

def user_landing(request):
    userId = request.session.get("user_id")
    if not userId:
        logout(request)
        return redirect("/seva/login/")
    contextDict = {}
    contextDict = utils.get_user_with_id(userId)
    searchName = request.GET.get('name', '')
    searchProfession = request.GET.get('profession', '')
    searchLocation = request.GET.get('location', '')
    searchResults = search_user_helper(userId, searchName, searchProfession, searchLocation)
    contextDict.update(searchResults)
    return render(request, "sevalinks/user_landing.html", contextDict)

def search_user_helper(user_id, searchName, searchProfession, searchLocation):
    users = []
    if searchName or (searchProfession and searchLocation):
        searchUsers = search_handler.Search(str(user_id), 0, 10, 10)
        searchUsers.construct_query(searchName, searchProfession, searchLocation)
        users = searchUsers.search_user()
    print users
    searchResults = {"searchResults":users, "searchName":searchName,
                     "searchProfession":searchProfession, "searchLocation":searchLocation}
    return searchResults

def user_find(request):
    contextDict = {}
    searchName = ""
    searchProfession = ""
    searchLocation = ""
    if request.method == "POST":
        print request.POST
        searchName = request.POST.get('search_name', '')
        searchProfession = request.POST.get('search_profession', '')
        searchLocation = request.POST.get('search_location', '')
    else:
        searchName = request.GET.get('name', '')
        searchProfession = request.GET.get('profession', '')
        searchLocation = request.GET.get('location', '')
    searchResults = search_user_helper("", searchName, searchProfession, searchLocation)
    contextDict.update(searchResults)
    return render(request, "sevalinks/user_find.html", contextDict)

def add_location(request):
    contextDict = {}
    userId = request.session.get("user_id")
    if not userId:
        logout(request)
        return redirect("/seva/login/")
    if request.method == "POST":
        editInfo = request.POST.dict()
        print editInfo
        if set(configs.USER_LOCATION_EDIT_FIELDS).issubset(editInfo):
            editStatus = utils.validate_location(editInfo)
            if editStatus == 1:
                print "====updating user===="
                editInfo["user_id"] = userId
                editInfo["user_area"] = (editInfo["user_area"]).title()
                updateStatus = utils.update_location(editInfo)
                return redirect("/seva/myaccount/")
            else:
                contextDict = editInfo
                contextDict['validation_error'] = editStatus
                return render(request, "sevalinks/add_location.html", contextDict)
    contextDict.update(utils.get_location_as_dict(request.session["user_id"]))
    contextDict.update(utils.get_user_image_as_dict(userId))
    return render(request, "sevalinks/add_location.html", contextDict)

def add_image(request):
    userId = request.session.get("user_id")
    if not userId:
        logout(request)
        return redirect("/seva/login/")
    if request.method == "POST":
        #imageForm = forms.ImageUploadForm(request.POST, request.FILES)
        #if imageForm.is_valid():
        imageName = image_handler.save_from_base64(request.POST)
        utils.update_user_image(request.session["user_id"], imageName)
        return render(request, "sevalinks/changeimage.html", {"image_status": "success"})
    return redirect("/seva/changeimage/")

def add_education(request):
    contextDict = {}
    userId = request.session.get("user_id")
    if not userId:
        logout(request)
        return redirect("/seva/login/")
    if request.method == "POST":
        editInfo = request.POST.dict()
        print editInfo
        if set(configs.USER_LOCATION_EDIT_FIELDS).issubset(editInfo):
            editStatus = utils.validate_location(editInfo)
            if editStatus == 1:
                print "====updating user===="
                editInfo["user_id"] = userId
                editInfo["user_area"] = (editInfo["user_area"]).title()
                updateStatus = utils.update_location(editInfo)
                return redirect("/seva/myaccount/")
            else:
                contextDict = editInfo
                contextDict['validation_error'] = editStatus
                return render(request, "sevalinks/add_location.html", contextDict)
    contextDict.update(utils.get_location_as_dict(request.session["user_id"]))
    contextDict.update(utils.get_user_image_as_dict(userId))
    return render(request, "sevalinks/add_location.html", contextDict)

def add_profession(request):
    contextDict = {}
    userId = request.session.get("user_id")
    if not userId:
        logout(request)
        return redirect("/seva/login/")
    if request.method == "POST":
        editInfo = request.POST.dict()
        print editInfo
        if set(configs.USER_PROFESSION_EDIT_FIELDS).issubset(editInfo):
            editStatus = utils.validate_profession(editInfo)
            print editStatus
            if editStatus == 1:
                print "====updating user===="
                editInfo["user_id"] = userId
                updateStatus = utils.update_profession(editInfo)
                return redirect("/seva/myaccount/")
            else:
                contextDict = editInfo
                contextDict['validation_error'] = editStatus
                return render(request, "sevalinks/user_profession.html", contextDict)
    print utils.get_profession_as_dict(request.session["user_id"])
    contextDict.update(utils.get_profession_as_dict(request.session["user_id"]))
    contextDict.update(utils.get_user_image_as_dict(userId))
    return render(request, "sevalinks/user_profession.html", contextDict)

def api_notification_check(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    try:
        noticeList = []
        contactManager = ContactsManager()
        notice = contactManager.check_notification(userOneId)
        print notice
        for eachNotice in notice:
            noticeDict = {}
            noticeDict["DESCRIPTION"] = configs.NOTIFICATION_DESCRIPTION[str(eachNotice["description_id"])]
            noticeDict["CATEGORY"] = configs.NOTIFICATION_CATEGORY[str(eachNotice["category_id"])]
            noticeDict["DESCRIPTION_TYPE"] = configs.NOTIFICATION_DESCRIPTION_TYPE[str(eachNotice["description_id"])]
            noticeDict["SOURCE"] = utils.get_user_with_id(eachNotice["source_id"])
            noticeList.append(noticeDict)
            print noticeDict
        responseDict["NOTIFICATION"] = noticeList
    except Exception as e:
        print e
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Invalid request"
    return JsonResponse(responseDict)

def api_notification_ack(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    if request.method == "POST":
        try:
            category = request.POST.get('category', '')
            contactManager = ContactsManager()
            notice = contactManager.ack_notification(userOneId, category)
        except Exception as e:
            print e
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request"
    return JsonResponse(responseDict)
