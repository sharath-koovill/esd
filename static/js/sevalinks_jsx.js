var users;


$(document).ready(function(){
  $.ajax({
        url: '/contacts/connections_json/',
        type: "GET",
        dataType: 'json',
        success: function (data) {
            users = data["CONNECTIONS"];
            }
    });
});


function formatName(users) {
  return users.first_name + ' ' + users.last_name;
}



const element = (
  <h1>
    Hello, {formatName(users)}!
  </h1>
);

ReactDOM.render(
  element,
  document.getElementById('root')
);
