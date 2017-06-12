import sys
from django.shortcuts import render, redirect
from django.http import JsonResponse
from contacts.manager import ContactsManager
import sevalinks.utils as utils
# Create your views here.

def other_profile(request):
    contextDict = {}
    userIdentifier = request.GET.get('user', '')
    if userIdentifier != '':
        userId = utils.get_userid_from_identifier(userIdentifier)
        contextDict = utils.get_user_with_id(userId)
        contextDict.update(utils.get_user_location_with_id(userId))
        contextDict.update(utils.get_user_profession_with_id(userId))
        contextDict.update(utils.get_user_image_as_dict(userId))
        return render(request, "sevalinks/other_profile.html", contextDict)
    else:
        return redirect("/404/")

def user_connections(request):
    contextDict = {}
    return render(request, "sevalinks/user_contacts.html", contextDict)

def api_user_connections(request):
    responseDict = {"STATUS":"success", "REASON":"good"}
    userOneId = request.session.get("user_id")
    if not userOneId:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "UnIdentified user"
    try:
        contactManager = ContactsManager()
        contacts = contactManager.friends(userOneId)
        print contacts
        responseDict["CONNECTIONS"] = contacts
    except:
        print sys.exc_info()[0]
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Invalid request"

    return JsonResponse(responseDict)

def api_user_invitations(request):
    responseDict = {"STATUS":"success", "REASON":"good"}
    userOneId = request.session.get("user_id")
    if not userOneId:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "UnIdentified user"
    try:
        contactManager = ContactsManager()
        contacts = contactManager.invitations(userOneId)
        print contacts
        responseDict["CONNECTIONS"] = contacts
    except:
        print sys.exc_info()[0]
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Invalid request"

    return JsonResponse(responseDict)

def api_blocked_users(request):
    responseDict = {"STATUS":"success", "REASON":"good"}
    userOneId = request.session.get("user_id")
    if not userOneId:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "UnIdentified user"
    try:
        contactManager = ContactsManager()
        contacts = contactManager.blocked_users(userOneId)
        print contacts
        responseDict["CONNECTIONS"] = contacts
    except:
        print sys.exc_info()[0]
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Invalid request"

    return JsonResponse(responseDict)

def api_block_user(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    userIdentifier = request.GET.get('user')
    if request.method == "POST" or userIdentifier:
        print request.POST
        try:
            userTwoId = utils.get_userid_from_identifier(userIdentifier)
            contactManager = ContactsManager()
            contactManager.block(userOneId, userTwoId, userOneId)
        except:
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request or Invalid User"
    return JsonResponse(responseDict)

def api_unblock_user(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    userIdentifier = request.GET.get('user')
    if request.method == "POST" or userIdentifier:
        print request.POST
        try:
            userTwoId = utils.get_userid_from_identifier(userIdentifier)
            contactManager = ContactsManager()
            contactManager.unblock(userOneId, userTwoId, userOneId)
        except:
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request or Invalid User"
    return JsonResponse(responseDict)

def api_request_connection(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    userIdentifier = request.GET.get('user', '')
    if request.method == "POST" or userIdentifier:
        print request.POST
        try:
            userTwoId = utils.get_userid_from_identifier(userIdentifier)
            contactManager = ContactsManager()
            contactManager.invite(userOneId, userTwoId, userOneId)
        except Exception as e:
            print e
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request or Invalid User"
    return JsonResponse(responseDict)

def api_accept_connection(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    userIdentifier = request.GET.get('user', '')
    if request.method == "POST" or userIdentifier:
        print request.POST
        try:
            userTwoId = utils.get_userid_from_identifier(userIdentifier)
            contactManager = ContactsManager()
            contactManager.accept_invitation(userOneId, userTwoId, userTwoId)
        except Exception as e:
            print e
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request or Invalid User"
    return JsonResponse(responseDict)

def api_decline_connection(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    userIdentifier = request.GET.get('user', '')
    if request.method == "POST" or userIdentifier:
        print request.POST
        try:
            userTwoId = utils.get_userid_from_identifier(userIdentifier)
            contactManager = ContactsManager()
            contactManager.decline(userOneId, userTwoId, userOneId)
        except:
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request or Invalid User"
    return JsonResponse(responseDict)

def api_remove_connection(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    userIdentifier = request.GET.get('user', '')
    if request.method == "POST" or userIdentifier:
        print request.POST
        try:
            userTwoId = utils.get_userid_from_identifier(userIdentifier)
            contactManager = ContactsManager()
            contactManager.remove(userOneId, userTwoId)
        except:
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request or Invalid User"
    return JsonResponse(responseDict)

def api_connection_count(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    userIdentifier = request.GET.get('user', '')
    if userIdentifier != '':
        try:
            userId = utils.get_userid_from_identifier(userIdentifier)
            contactManager = ContactsManager()
            responseDict["COUNT"] = contactManager.connection_count(userId)
        except Exception as e:
            print e
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "User Identifier not specified"
    return JsonResponse(responseDict)

def api_connection_check(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    userIdentifier = request.GET.get('user', '')
    if userIdentifier != '':
        try:
            userTwoId = utils.get_userid_from_identifier(userIdentifier)
            contactManager = ContactsManager()
            responseDict["CONNECTION_STATUS"] = contactManager.check_connection(userOneId, userTwoId)
        except Exception as e:
            print e
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "User Identifier not specified"
    return JsonResponse(responseDict)
