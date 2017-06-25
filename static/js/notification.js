$(document).ready(function () {
  getNotifications();
});

function getNotifications() {
  $.ajax({
    url: '/seva/notification_check/',
    type: "GET",
    dataType: 'json',
    success: function success(data) {
      if (Object.keys(data["NOTIFICATION"]).length > 0) {
        notifyConnections(data["NOTIFICATION"]);
      }
    }
  });
}

function notifyConnections(notices) {
  var notificationCount = 0;
  var cnt = Object.keys(notices).length;
  for (var i=0; i<cnt; i++){
    if (notices[i]["DESCRIPTION_TYPE"] == "INVITATION ACCEPT" || notices[i]["DESCRIPTION_TYPE"] == "INVITATION"){
      notificationCount = notificationCount + 1;
    }
  }
  if(notificationCount > 0){
    var noticeHtml = getNoticeHTML(notificationCount);
    $(".connections_notify").html(noticeHtml);
  }
}

function notifyUser(){
  $('#notification_on').show();
  $('#notification_off').hide();
}

function renderNotifications(notices) {
  var descriptor0Flag = false;
  var descriptor1Flag = false;
  var cnt = Object.keys(notices).length;
  var noticeHtml = "";
  for (var i=0; i<cnt; i++){
    if (!descriptor0Flag && notices[i]["DESCRIPTION_TYPE"] == "INVITATION"){
      descriptor0Flag = true;
      noticeHtml = noticeHtml + getEachNotice(notices[i]["CATEGORY"], notices[i]["DESCRIPTION"]);
    }
    if (!descriptor1Flag && notices[i]["DESCRIPTION_TYPE"] == "INVITATION ACCEPT"){
      descriptor1Flag = true;
      noticeHtml = noticeHtml + getEachNotice(notices[i]["CATEGORY"], notices[i]["DESCRIPTION"]);
    }
  }
  $("#dropdown_1").html(noticeHtml);
}

function getNoticeHTML(count){
  var element = "Connections<span onclick='notificationAcknowledge(0)' class='new badge red'>"+ count +"</span>";
  return element;
}

function getEachNotice(count){
  var element = "Connections<span onclick='notificationAcknowledge(0)' class='new badge red'>"+ count +"</span>";
  return element;
}


function notificationAcknowledge(category_id) {
  alert(category_id);
  var ajaxUrl = '/seva/notification_ack/';
  var postData = {"csrfmiddlewaretoken" : $("input[name=csrfmiddlewaretoken]").val(), "category": category_id };
  $.ajax({
    url: ajaxUrl,
    type: "POST",
    data: postData,
    dataType: 'json',
    success: function success(data) {

    }
  });
}
