$(document).ready(function () {
  getConnectionCount();
  checkUserConnection();
});

function getConnectionCount() {
  var ajaxUrl = '/contacts/connection_count/' + $(location).attr('search');
  $.ajax({
    url: ajaxUrl,
    type: "GET",
    dataType: 'json',
    success: function success(data) {
      renderCount(data["COUNT"]);
    }
  });
}

function sendConnectionInvite() {
  var ajaxUrl = '/contacts/connection_send/' + $(location).attr('search');
  var postData = {"csrfmiddlewaretoken" : $("input[name=csrfmiddlewaretoken]").val() };
  $.ajax({
    url: ajaxUrl,
    type: "POST",
    data: postData,
    dataType: 'json',
    success: function success(data) {
      renderConnectionCheck(0);
    }
  });
}

function acceptConnectionInvite() {
  var ajaxUrl = '/contacts/connection_accept/' + $(location).attr('search');
  var postData = {"csrfmiddlewaretoken" : $("input[name=csrfmiddlewaretoken]").val() };
  $.ajax({
    url: ajaxUrl,
    type: "POST",
    data: postData,
    dataType: 'json',
    success: function success(data) {
      renderConnectionCheck(1);
      getConnectionCount();
    }
  });
}

function checkUserConnection() {
  var ajaxUrl = '/contacts/connection_check/' + $(location).attr('search');
  $.ajax({
    url: ajaxUrl,
    type: "GET",
    dataType: 'json',
    success: function success(data) {
      renderConnectionCheck(data["CONNECTION_STATUS"]);
    }
  });
}

function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

var connectionMap = new Map();
connectionMap["-1"] = "#connection_off";
connectionMap["2"] = "#connection_off";
connectionMap["1"] = "#connection_on";
connectionMap["0"] = "#connection_sent";
connectionMap["4"] = "#connection_received";

function renderConnectionCheck(status){
  status = status.toString();
  for (var ky in connectionMap){
    if (connectionMap[status] == connectionMap[ky]){
      $(connectionMap[ky]).show();
    }
    else{
         $(connectionMap[ky]).hide();
    }
  }
  // alert(status);
  // Object.keys(connectionMap).forEach(function(ky) {
  //   alert(connectionMap[status]);
  //   if (connectionMap[status] == connectionMap[ky]){
  //     alert(connectionMap[ky]);
  //     $(connectionMap[status]).show();
  //   }
  //   else{
  //     $(connectionMap[status]).hide();
  //   }
  // });
}

function renderCount(count){
  $("#connection_count").text(String(count));
}
