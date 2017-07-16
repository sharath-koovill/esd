$(document).ready(function () {
  $("#message_history").hide();
  getContacts();
  if ($("#message_section").html() == "Inbox"){
    getReceivedMessages();
  }
  else{
    getSentMessages();
  }
});

function getContacts() {
  $.ajax({
    url: '/contacts/connections_json/',
    type: "GET",
    dataType: 'json',
    success: function success(data) {
      if (Object.keys(data["CONNECTIONS"]).length > 0) {
        populateContacts(data["CONNECTIONS"]);
      }
    }
  });
}

function populateContacts(users){
  var allConn = "";
  jQuery.each(users, function() {
    allConn = allConn + renderEmpty(JSON.stringify(this["u_user_id"]), formatName(this));
  });
  allConn = allConn + renderEmpty("3", "qwer tyu");
  allConn = allConn + renderEmpty("4", "qwer1 tyu2");
  $("#message_connections").html(allConn);
}

function formatName(users) {
  return users["u_first_name"] + " " + users["u_last_name"];
}

function renderEmpty(id, name) {
  return "<option value="+ id +">"+ name +"</option>";
}

function sendMessage() {
  var e = document.getElementById("message_connections");
  var targetId = e.options[e.selectedIndex].value;
  var message = $("#message_text").val();
  if (message != ""){
    postMessage(targetId, message);
    alert("Message Sent");
    return true;
  }
  else{
    alert("Empty message. Please enter a valid message.");
    return false;
  }

}

function postMessage(targetId, message) {
  var ajaxUrl = '/contacts/message_send/';
  var postData = {"csrfmiddlewaretoken" : $("input[name=csrfmiddlewaretoken]").val(), "message": message,
                  "target_id": targetId};
  $.ajax({
    url: ajaxUrl,
    type: "POST",
    data: postData,
    dataType: 'json',
    success: function success(data) {
      return true;
    }
  });
}


function getReceivedMessages() {
  $.ajax({
    url: '/contacts/message_received/',
    type: "GET",
    dataType: 'json',
    success: function success(data) {
      if (Object.keys(data["MESSAGES"]).length > 0) {
        storeMessages(data["MESSAGES"]);
      }
    }
  });
}

function getSentMessages() {
  $.ajax({
    url: '/contacts/message_sent/',
    type: "GET",
    dataType: 'json',
    success: function success(data) {
      if (Object.keys(data["MESSAGES"]).length > 0) {
        storeMessages(data["MESSAGES"]);
      }
    }
  });
}

function renderConversations(user) {
  var convList = "<li class='collection-item'><div>";
  convList = convList + "<h6>" + user["first_name"] + " " + user["last_name"] + "</h6>";
  convList = convList + "<label>" + user["send_date"].split(".")[0] + "</label>";
  convList = convList + "<a id='" + user["id"] + "' href='#!' onclick='getMessagesFromSession(this.id)' class='secondary-content'><i class='material-icons'>send</i></a>";
  convList = convList + "</div></li>";
  return convList;
}

function storeMessages(data){
  var conv = "";
  jQuery.each(data, function() {
    sessionStorage.setItem(JSON.stringify(this["id"]), JSON.stringify(this));
    conv = conv + renderConversations(this);
  });
  $("#message_conversations").html(conv);
}

function getMessagesFromSession(id){
  $("#message_history").show();
  var data = sessionStorage.getItem(id);
  var jsonData = JSON.parse(data);
  var msg = jsonData["message"];
  var sentDate = jsonData["send_date"].split(".");
  var user = jsonData["first_name"] + " " + jsonData["last_name"];
  $("#from").html(user);
  $("#sent_time").html(sentDate[0]);
  $("#message_view").html(msg);
  if ($("#message_section").html() == "Inbox"){
    $("#reply_id").val(jsonData["source_id"]);
  }
  else{
    $("#reply_id").val(jsonData["target_id"]);
  }


}

function setReplyId(){
  var userID = $("#reply_id").val();
  $("#message_connections").val(userID).trigger('change');
}


// function createOrOpenDB(connections){
//   Dexie.delete('sevalinks');
//   // var db = new Dexie("sevalinks");
//   // db.version(1).stores({
//   // contacts: 'u_user_id,u_first_name,u_last_name,u_username,u_user_image,u_user_profession,u_user_area,u_user_identifier,u_user_college_active'
//   // });
//   // jQuery.each(connections, function() {
//   //   db.contacts.put(this);
//   // });
//   // return db;
//
// }

// db.contacts.put({user_id:"3", first_name: "Josephine",
//          last_name: "Josephinew", username: "Josephine4",
//          user_image: "default_user.png", user_profession: "doctor",
//          user_area: "mangalore", user_identifier: "dfmf8ghw00w8hf"});
// {"STATUS": "success", "CONNECTIONS": [{"u_last_name": "Efgh", "u_username": "wewtsdgh", "u_first_name": "Abcd",
// "u_user_image": null, "u_user_id": 2, "u_user_profession": null,
// "u_user_identifier": "4cef3bad4a1b4a9aa50ccb09dec76cf8", "u_user_college_active": null, "u_user_area": null}], "REASON": "good"}

// function searchContacts(searchKey){
//   var db = new Dexie("sevalinks");
//   db.version(1).stores({
//   contacts: 'u_user_id,u_first_name,u_last_name,u_username,u_user_image,u_user_profession,u_user_area,u_user_identifier,u_user_college_active'
//   });
//   var sevacontact = db.contacts.where("u_first_name").startsWithIgnoreCase(searchKey).or("u_last_name").startsWithIgnoreCase(searchKey);
//   sevacontact.each(function(friend) {
//     alert(friend.u_username);
//     if (friend.u_username == "Josephine4"){
//       alert(friend.u_username);
//     }
//   });
// }
