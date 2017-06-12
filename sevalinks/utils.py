import forms
import models
import configs
from django.core import validators
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
import lepl.apps.rfc3696 as rfc
from passlib.hash import pbkdf2_sha256 as hashPass
import uuid
import hashlib
import datetime

def validate_user(userData):
    if userData["username"] == None or userData["username"] == "":
        return "Username must not be empty"
    if len(str(userData["username"])) < 8:
        return "Username must have minimum 8 characters"
    if userData["email"] != userData["confirm_email"]:
        return "Emails do not match"
    email_validator = rfc.Email()    
    if not email_validator(userData["email"]):
        return "Invalid email"
    if userData["password"] != userData["confirm_password"]:
        return "Passwords do not match"
    if not(len(str(userData["phone_number"])) == 10):
        return "Incorrect Phone number"
    if models.User.objects.filter(email=userData["email"]).exists():
        return "Email already registered"
    return 1

def validate_email(email):
    email_validator = rfc.Email()    
    if email == "" or not (email_validator(email)):
        return "You have provided an invalid email."
    if not models.User.objects.filter(email=email).exists():
        return "Sorry, this email is not registered."
    return 1

def add_reset_password_id(userId, resetId):    
    user = models.UserResetPassword(user_id=get_user(userId), reset_id=resetId)
    user.save()
    
def add_confirmation_id(userId, confirmId):        
    user = models.UserConfirmation(user_id=get_user(userId), user_confirmation_id=confirmId)
    user.save()

def get_user_from_resetpassword(resetId):
    try:    
        user = models.UserResetPassword.objects.get(reset_id=resetId)
        return user
    except ObjectDoesNotExist:
        return None    

def get_user_from_confirmation(confirmId):
    try:    
        user = models.UserConfirmation.objects.get(user_confirmation_id=confirmId)
        return user
    except ObjectDoesNotExist:
        return None
    
def update_reset_password_id(userId, resetId):    
    user = models.UserResetPassword(user_id=userId, reset_id=resetId)
    user.save()

def save_user_image(userId, imageName):
    user = models.UserImage(user_id=get_user(userId), user_image=imageName)
    user.save()
    
def update_user_image(userId, imageName):
    try:
        user = models.UserImage.objects.get(user_id=get_user(userId))
        user.user_image = imageName
        user.save()
    except ObjectDoesNotExist:
        save_user_image(userId, imageName)

def get_user_image_as_dict(userId):    
    user = models.UserImage.objects.filter(user_id_id=userId).values()
    if len(user) > 0:
        user[0]["user_image"] = "/" + user[0]["user_image"]
        return user[0]   
    return {}    

def get_userid_from_identifier(identifier):
    user = models.User.objects.filter(user_identifier=identifier).values()
    print user
    return user[0]["user_id"]
    
def save_user(userData):
    hashedPass = hashPass.hash(userData["password"])
    user = models.User(first_name=(userData["first_name"]).title(), last_name=(userData["last_name"]).title(), 
                       username=userData["username"], email=userData["email"],
                       password=hashedPass, phone_number=userData["phone_number"])
    user.save()
    
def save_user_temp(userData):
    hashedPass = hashPass.hash(userData["password"])
    user = models.User(first_name=(userData["first_name"]).title(), last_name=(userData["last_name"]).title(), 
                       username=userData["username"], email=userData["email"], 
                       password=hashedPass, phone_number=userData["phone_number"], user_active=True)
    user.save()

def update_user(userData, userFields=configs.USER_EDIT_FIELDS):
    user = models.User.objects.get(user_id=userData["user_id"])    
    for eachField in userFields:
        setattr(user, eachField, userData[eachField])
    user.save()

def save_user_profession(userData):
    user = models.UserProfession(user_id=get_user(userData["user_id"]), user_job_designation=userData["user_job_designation"],
                               user_experience=userData["user_experience"], user_industry=userData["user_industry"],
                               user_company=userData["user_company"], user_description=userData["user_description"],
                               user_profession=userData["user_profession"])    
    user.save()

def update_profession(userData, userFields=configs.USER_PROFESSION_EDIT_FIELDS):
    try:
        user = models.UserProfession.objects.get(user_id=get_user(userData["user_id"]))    
        for eachField in userFields:
            setattr(user, eachField, userData[eachField])
        user.save()
    except ObjectDoesNotExist:
        save_user_profession(userData)
        
def get_user_profession_with_id(userId):
    """
    used in myaccount section
    """
    user = models.UserProfession.objects.filter(user_id=userId).values()
    if len(user) > 0:
        changeFields = [configs.INDUSTRY, configs.DESIGNATION, configs.EXPERIENCE]
        changeKeys = ["user_industry", "user_job_designation", "user_experience"]
        for eachField, eachKey in zip(changeFields, changeKeys):
            for code, name in eachField:
                if code == user[0][eachKey]:
                    user[0][eachKey] = name    
        return user[0]
    return {}

def get_profession_as_dict(userId):
    """
    used in edit profession section
    """
    user = models.UserProfession.objects.filter(user_id_id=userId).values()
    if len(user) > 0:
        return user[0]   
    return {}

def save_user_location(userData):
    user = models.UserLocation(user_id=get_user(userData["user_id"]), user_country=userData["user_country"],
                               user_state=userData["user_state"],
                               user_area=userData["user_area"], user_postcode=userData["user_postcode"])    
    user.save()

def update_location(userData, userFields=configs.USER_LOCATION_EDIT_FIELDS):
    try:
        user = models.UserLocation.objects.get(user_id=get_user(userData["user_id"]))    
        for eachField in userFields:
            setattr(user, eachField, userData[eachField])
        user.save()
    except ObjectDoesNotExist:
        save_user_location(userData)
        
def get_user_location_with_id(userId):
    """
    used in myaccount section
    """
    user = models.UserLocation.objects.filter(user_id=userId).values()
    if len(user) > 0:
        for code, name in configs.STATES:
            if code == user[0]["user_state"]:
                 user[0]["user_state"] = name    
        return user[0]
    return {}

def get_location_as_dict(userId):
    """
    used in edit profession section
    """
    user = models.UserLocation.objects.filter(user_id_id=userId).values()
    if len(user) > 0:
        return user[0]   
    return {}    
    
def get_user(userId):
    user = models.User.objects.get(user_id=userId)
    return user

def get_user_as_dict(email):
    user = models.User.objects.filter(email=email).values()[0]
    return user

def get_user_with_id(userId):
    user = models.User.objects.filter(user_id=userId).values()[0]
    return user

def authenticate_session(request):
    userId = request.session.get("user_id")
    if userId and models.User.objects.filter(user_id=userId).exists():
        return True
    else:
        return False

def create_random_identifier():
    return str(uuid.uuid4()) + hashlib.sha224(str(datetime.datetime.now())).hexdigest()


def authenticate_user(email, password):
    if models.User.objects.filter(email=email).exists():
        user = get_user_as_dict(email)
        try:
            if hashPass.verify(password, user["password"]):
                return 1
        except ValueError:
            return 0    
    return 0
        
def validate_edit_user(userData):
    if userData["first_name"] == None or userData["first_name"] == "":
        return "First name must not be empty"
    if userData["last_name"] == None or userData["last_name"] == "":
        return "Last name must not be empty"
    if not(len(str(userData["phone_number"])) == 10):
        return "Incorrect Phone number"
    return 1

def validate_location(userData):
    if userData["user_country"] == None or userData["user_country"] == "":
        return "Country must not be empty"
    if userData["user_state"] == None or userData["user_state"] == "":
        return "State must not be empty"
    if userData["user_area"] == None or userData["user_area"] == "":
        return "Area must not be empty"
    if userData["user_postcode"] == None or userData["user_postcode"] == "":
        return "Pincode must not be empty"
    return 1

def validate_profession(userData):
    if userData["user_profession"] == None or userData["user_profession"] == "":
        return "Profession must not be empty"
    if userData["user_experience"] == None or userData["user_experience"] == "":
        return "Experience must not be empty"
    #if userData["user_industry"] == None or userData["user_industry"] == "":
        #return "Industry must not be empty"
    #if userData["user_company"] == None or userData["user_company"] == "":
        #return "Company must not be empty"
    #if userData["user_description"] == None or userData["user_description"] == "":
        #return "Please provide some description about yourself."
    return 1

def user_search(profession="Football",name="sharath",area="udupi"):
    #user = models.User.objects.filter(Q(first_name__contains=name) & Q(last_name__contains=name))
    userFromLocation = models.UserLocation.objects.filter(Q(user_area__contains=area) | Q(user_state__contains=area))    
    userFromLocation = models.UserLocation.objects.filter((Q(user__first_name__contains=name) | Q(user__last_name__contains=name)) & (Q(user_area__contains=area) | Q(user_state__contains=area))).select_related()
    print userFromLocation.values()
    print "location:==========================="
    userFromProfession = models.UserProfession.objects.filter(user_profession__contains=profession).select_related()
    print userFromProfession.values()
    print "profession:==========================="
    user = userFromLocation | userFromProfession
    user = user.distinct()
    userFinal = user.filter(Q(first_name__contains=name) | Q(last_name__contains=name))    
    return userFinal