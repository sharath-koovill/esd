'use strict';

var users;

$(document).ready(function () {
  getConnections();
});

function getConnections() {
  $.ajax({
    url: '/contacts/connections_json/',
    type: "GET",
    dataType: 'json',
    success: function success(data) {
      if (Object.keys(data["CONNECTIONS"]).length > 0){
      renderContacts(data["CONNECTIONS"]);
      }
      else {
        renderEmpty("You don't seem to have any Connections.");
      }
    }
  });
}

function getInvitations() {
  $.ajax({
    url: '/contacts/connections_json/',
    type: "GET",
    dataType: 'json',
    success: function success(data) {
      if (Object.keys(data["CONNECTIONS"]).length > 0){
      renderContacts(data["CONNECTIONS"]);
      }
      else {
        renderEmpty("You don't seem to have any Connection Invitations.");
      }
    }
  });
}

function getBlockedUsers() {
  $.ajax({
    url: '/contacts/connections_json/',
    type: "GET",
    dataType: 'json',
    success: function success(data) {
      if (Object.keys(data["CONNECTIONS"]).length > 0){
      renderContacts(data["CONNECTIONS"]);
      }
      else {
        renderEmpty("You don't seem to have any Blocked Users.");
      }
    }
  });
}

function formatName(users) {
  return users["first_name"] + " " + users["last_name"];
}

function renderEmpty(message){
  var element = React.createElement(
    "div",
    { "class": "row" },
    React.createElement(
      "div",
      { "class": "col" },
      React.createElement(
        "label",
        null,
      message
    )
  )
);
  ReactDOM.render(element, document.getElementById('user_container'));
}

function renderContacts(users){
  var element = React.createElement(
    'h1',
    null,
    'Hello, ',
    formatName(users),
    '!'
  );
  ReactDOM.render(element, document.getElementById('user_container'));
}

class Connection extends React.Component {
  constructor(props) {
    super(props);
  }

  userImage(){
    var userImage = this.props.user_image;
    if(userImage != "")
    {
      return "/static/userimages/" + userImage;
    }
    else{
      return "/static/userimages/default_user.png";
    }
  }

  render() {
    return (
      <div class="userchip">
      <img src="{this.userImage}" />
        <div>
          <a href="{this.props.user_identifier}">{this.props.first_name} {this.props.last_name}</a>
          <label>{this.props.user_profession}, {this.props.user_area}</label>
          <span>{this.props.subscription_name}</span>
        </div>
     </div>
   )
  }
}

function RenderConnections(users){
  var element = React.createClass({
    render: function() {
      return (
        <div class="row">
        {users.map(function(eachuser){
            return <Connection user_image={eachuser["u_user_image"]}
            user_identifier={eachuser["u_user_identifier"]}
            first_name={eachuser["u_first_name"]}
            last_name={eachuser["u_last_name"]}
            user_profession={eachuser["u_user_profession"]}
            user_area={eachuser["u_user_area"]}
            subscription_name={eachuser["u_subscription_name"]} />;
            })}
         </div>
       )
     }
   });
  ReactDOM.render(element, document.getElementById('user_container'));
}

// function RenderConnections1(users){
// return users.map((eachuser) =>
//   <Connection user_image=eachuser["u_user_image"]
//   user_identifier=eachuser["u_user_identifier"]
//   first_name=eachuser["u_first_name"]
//   last_name=eachuser["u_last_name"]
//   user_profession=eachuser["u_user_profession"]
//   user_area=eachuser["u_user_area"]
//   subscription_name=eachuser["u_subscription_name"]
//   />
// );
// }
