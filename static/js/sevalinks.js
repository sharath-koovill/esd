'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

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
      if (Object.keys(data["CONNECTIONS"]).length > 0) {
        renderConnectionsHB(data["CONNECTIONS"]);
      } else {
        renderEmpty("You don't seem to have any Connections.");
      }
    }
  });
}

function getInvitations() {
  $.ajax({
    url: '/contacts/invitations_json/',
    type: "GET",
    dataType: 'json',
    success: function success(data) {
      if (Object.keys(data["CONNECTIONS"]).length > 0) {
        renderConnectionsHB(data["CONNECTIONS"]);
      } else {
        renderEmpty("You don't seem to have any Connection Invitations.");
      }
    }
  });
}

function getBlockedUsers() {
  $.ajax({
    url: '/contacts/blocked_json/',
    type: "GET",
    dataType: 'json',
    success: function success(data) {
      if (Object.keys(data["CONNECTIONS"]).length > 0) {
        renderConnectionsHB(data["CONNECTIONS"]);
      } else {
        renderEmpty("You don't seem to have any Blocked Users.");
      }
    }
  });
}

function renderConnectionsHB(users) {
  var source = $("#connection-template").html();
  var tlate = Handlebars.compile(source);
  var allConn = "";
  jQuery.each(users, function() {
    allConn = allConn + tlate(this);    
  });
  $("#user_container").html(allConn);
}

function formatName(users) {
  return users["first_name"] + " " + users["last_name"];
}

function renderEmpty(message) {
  var element = "<div class='col'><label>" + message + "</label></div>"
  $("#user_container").html(element);
}

function renderEmpty1(message) {
  var element = React.createElement("div", { "class": "row" }, React.createElement("div", { "class": "col" }, React.createElement("label", null, message)));
  ReactDOM.render(element, document.getElementById('user_container'));
}

function renderContacts(users) {
  var element = React.createElement('h1', null, 'Hello, ', formatName(users), '!');
  ReactDOM.render(element, document.getElementById('user_container'));
}

var Connection = function (_React$Component) {
  _inherits(Connection, _React$Component);

  function Connection(props) {
    _classCallCheck(this, Connection);

    return _possibleConstructorReturn(this, (Connection.__proto__ || Object.getPrototypeOf(Connection)).call(this, props));
  }

  _createClass(Connection, [{
    key: 'userImage',
    value: function userImage() {
      var userImage = this.props.user_image;
      if (userImage != "") {
        return "/static/userimages/" + userImage;
      } else {
        return "/static/userimages/default_user.png";
      }
    }
  }, {
    key: 'render',
    value: function render() {
      return React.createElement(
        'div',
        { 'class': 'userchip' },
        React.createElement('img', { src: '{this.userImage}' }),
        React.createElement(
          'div',
          null,
          React.createElement(
            'a',
            { href: '{this.props.user_identifier}' },
            this.props.first_name,
            ' ',
            this.props.last_name
          ),
          React.createElement(
            'label',
            null,
            this.props.user_profession,
            ', ',
            this.props.user_area
          ),
          React.createElement(
            'span',
            null,
            this.props.subscription_name
          )
        )
      );
    }
  }]);

  return Connection;
}(React.Component);

function RenderConnections(users) {
  var element = React.createClass({
    displayName: 'element',

    render: function render() {
      return React.createElement(
        'div',
        { 'class': 'row' },
        users.map(function (eachuser) {
          return React.createElement(Connection, { user_image: eachuser["u_user_image"],
            user_identifier: eachuser["u_user_identifier"],
            first_name: eachuser["u_first_name"],
            last_name: eachuser["u_last_name"],
            user_profession: eachuser["u_user_profession"],
            user_area: eachuser["u_user_area"],
            subscription_name: eachuser["u_subscription_name"] });
        })
      );
    }
  });
  alert(element);
  ReactDOM.render(element, document.getElementById('user_container'));
}
