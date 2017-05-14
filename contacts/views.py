import sys
from django.shortcuts import render, redirect
from django.http import JsonResponse
from contacts.manager import ContactsManager

# Create your views here.

def other_profile(request):
    contextDict = {}
    return render(request, "sevalinks/other_profile.html", contextDict)

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
    if request.method == "POST":
        print request.POST
        try:
            userTwoId = request.POST.dict()["block_user_id"]
            contactManager = ContactsManager()
            contactManager.block(userOneId, userTwoId, userOneId)
        except:
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request"
    return JsonResponse(responseDict)

def api_unblock_user(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    if request.method == "POST":
        print request.POST
        try:
            userTwoId = request.POST.dict()["unblock_user_id"]
            contactManager = ContactsManager()
            contactManager.unblock(userOneId, userTwoId, userOneId)
        except:
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request"
    return JsonResponse(responseDict)

def api_request_connection(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    if request.method == "POST":
        print request.POST
        try:
            userTwoId = request.POST.dict()["request_user_id"]
            contactManager = ContactsManager()
            contactManager.invite(userOneId, userTwoId, userOneId)
        except:
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request"
    return JsonResponse(responseDict)

def api_accept_connection(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    if request.method == "POST":
        print request.POST
        try:
            userTwoId = request.POST.dict()["accept_user_id"]
            contactManager = ContactsManager()
            contactManager.accept_invitation(userOneId, userTwoId, userOneId)
        except:
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request"
    return JsonResponse(responseDict)

def api_decline_connection(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    if request.method == "POST":
        print request.POST
        try:
            userTwoId = request.POST.dict()["decline_user_id"]
            contactManager = ContactsManager()
            contactManager.decline(userOneId, userTwoId, userOneId)
        except:
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request"
    return JsonResponse(responseDict)

def api_remove_connection(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    if request.method == "POST":
        print request.POST
        try:
            userTwoId = request.POST.dict()["remove_user_id"]
            contactManager = ContactsManager()
            contactManager.remove(userOneId, userTwoId)
        except:
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request"
    return JsonResponse(responseDict)
