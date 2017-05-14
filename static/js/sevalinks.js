'use strict';

var users;

$(document).ready(function () {
  $.ajax({
    url: '/contacts/connections_json/',
    type: "GET",
    dataType: 'json',
    success: function success(data) {      
      renderContacts(data["CONNECTIONS"]);
    }
  });
});

function formatName(users) {
  return users["first_name"] + " " + users["last_name"];
}

function renderContacts(users){
  var element = React.createElement(
    'h1',
    null,
    'Hello, ',
    formatName(users),
    '!'
  );
  ReactDOM.render(element, document.getElementById('root'));
}
