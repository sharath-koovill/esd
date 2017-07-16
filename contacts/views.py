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

def api_send_message(request):
    userOneId = request.session.get("user_id", '')
    responseDict = {"STATUS":"success", "REASON":"good"}
    if request.method == "POST":
        print request.POST
        try:
            if not userOneId:
                userOneId = request.POST.get('source_id', '')
            userTwoId = request.POST.get('target_id', '')
            message = request.POST.get('message', '')
            if userOneId and userTwoId and message:
                contactManager = ContactsManager()
                contactManager.send_message(userOneId, userTwoId, message)
            else:
                raise Exception('POST data invalid')
        except Exception as e:
            print e
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "Not a POST request or Invalid User"
    return JsonResponse(responseDict)

def api_received_messages(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    # a = {"id":1, "send_date":"2017-06-25 20:57:44.129480", "source_id":33, "target_id":43, "first_name":"Shankar", "last_name":"Naidu", "user_identifier": "ibfdbfkdbfkbfk", "ack_date": "2017-06-25 20:57:44.129480","message":"bjbfabfasbfkbaskfbaskbkasbfkasbfkasbfkbaskfbaskbkasbkasbfkas"}
    # b = {"id":2, "send_date":"2017-06-24 20:57:44.129480", "source_id":34, "target_id":43, "first_name":"Shankar1", "last_name":"Naidu1", "user_identifier": "ibfdbfkdbfkbfk", "ack_date": "2017-06-24 20:57:44.129480", "message":"bjbfabfasbfkbaskfbaskbkasbfkasbfkasbfkbaskfbaskbkasbkasbfkas"}
    # c = {"id":3, "send_date":"2017-06-23 20:57:44.129480", "source_id":35, "target_id":43, "first_name":"Shankar2", "last_name":"Naidu2", "user_identifier": "ibfdbfkdbfkbfk", "ack_date": "2017-06-23 20:57:44.129480","message":"bjbfabfasbfkbaskfbaskbkasbfkasbfkasbfkbaskfbaskbkasbkasbfkas"}
    # d = {"id":4, "send_date":"2017-06-22 20:57:44.129480", "source_id":36, "target_id":43, "first_name":"Shankar3", "last_name":"Naidu3", "user_identifier": "ibfdbfkdbfkbfk", "ack_date": "2017-06-22 20:57:44.129480","message":"bjbfabfasbfkbaskfbaskbkasbfkasbfkasbfkbaskfbaskbkasbkasbfkas"}
    # responseDict["MESSAGES"] = [a, b, c, d]

    if userOneId != '':
        try:
            contactManager = ContactsManager()
            conv = contactManager.get_received_messages(userOneId)
            respList = []
            for eachConv in conv:
                user = utils.get_user_with_id(eachConv["source_id"])
                eachConv["first_name"] = user["first_name"]
                eachConv["last_name"] = user["last_name"]
                respList.append(eachConv)
            responseDict["MESSAGES"] = respList
        except Exception as e:
            print e
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "User Identifier not specified"
    return JsonResponse(responseDict)

def api_sent_messages(request):
    userOneId = request.session.get("user_id")
    responseDict = {"STATUS":"success", "REASON":"good"}
    # a = {"id":1, "send_date":"2017-06-25 20:57:44.129480", "source_id":33, "target_id":43, "first_name":"Shankar", "last_name":"Naidu", "user_identifier": "ibfdbfkdbfkbfk", "ack_date": "2017-06-25 20:57:44.129480","message":"bjbfabfasbfkbaskfbaskbkasbfkasbfkasbfkbaskfbaskbkasbkasbfkas"}
    # b = {"id":2, "send_date":"2017-06-24 20:57:44.129480", "source_id":33, "target_id":44, "first_name":"Shankar1", "last_name":"Naidu1", "user_identifier": "ibfdbfkdbfkbfk", "ack_date": "2017-06-24 20:57:44.129480", "message":"bjbfabfasbfkbaskfbaskbkasbfkasbfkasbfkbaskfbaskbkasbkasbfkas"}
    # c = {"id":3, "send_date":"2017-06-23 20:57:44.129480", "source_id":33, "target_id":45, "first_name":"Shankar2", "last_name":"Naidu2", "user_identifier": "ibfdbfkdbfkbfk", "ack_date": "2017-06-23 20:57:44.129480","message":"bjbfabfasbfkbaskfbaskbkasbfkasbfkasbfkbaskfbaskbkasbkasbfkas"}
    # d = {"id":4, "send_date":"2017-06-22 20:57:44.129480", "source_id":33, "target_id":46, "first_name":"Shankar3", "last_name":"Naidu3", "user_identifier": "ibfdbfkdbfkbfk", "ack_date": "2017-06-22 20:57:44.129480","message":"bjbfabfasbfkbaskfbaskbkasbfkasbfkasbfkbaskfbaskbkasbkasbfkas"}
    # e = {"id":5, "send_date":"2017-06-22 20:57:44.129480", "source_id":33, "target_id":46, "first_name":"Shankar3", "last_name":"Naidu3", "user_identifier": "ibfdbfkdbfkbfk", "ack_date": "2017-06-22 20:57:44.129480","message":"bjbfabfasbfkbaskfbaskbkasbfkasbfkasbfkbaskfbaskbkasbkasbfkas"}
    #
    # responseDict["MESSAGES"] = [a, b, c, d, e]

    if userOneId != '':
        try:
            contactManager = ContactsManager()
            conv = contactManager.get_sent_messages(userOneId)
            respList = []
            for eachConv in conv:
                user = utils.get_user_with_id(eachConv["target_id"])
                eachConv["first_name"] = user["first_name"]
                eachConv["last_name"] = user["last_name"]
                respList.append(eachConv)
            responseDict["MESSAGES"] = respList
        except Exception as e:
            print e
            responseDict["STATUS"] = "fail"
            responseDict["REASON"] = "Invalid request"
    else:
        responseDict["STATUS"] = "fail"
        responseDict["REASON"] = "User Identifier not specified"
    return JsonResponse(responseDict)
