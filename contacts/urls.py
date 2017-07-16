from django.conf.urls import url
import views

urlpatterns = [
    url(r'^profile/', views.other_profile, name="other_profile"),
    url(r'^connections/', views.user_connections, name="user_connections"),
    url(r'^invitations/', views.user_connections, name="user_connections"),
    url(r'^blocked/', views.user_connections, name="user_connections"),
    url(r'^connections_json/', views.api_user_connections, name="api_user_connections"),
    url(r'^invitations_json/', views.api_user_invitations, name="api_user_invitations"),
    url(r'^blocked_json/', views.api_blocked_users, name="api_blocked_users"),
    url(r'^connection_count/', views.api_connection_count, name="api_connection_count"),
    url(r'^connection_check/', views.api_connection_check, name="api_connection_check"),
    url(r'^connection_send/', views.api_request_connection, name="api_request_connection"),
    url(r'^connection_accept/', views.api_accept_connection, name="api_accept_connection"),
    url(r'^connection_decline/', views.api_decline_connection, name="api_decline_connection"),
    url(r'^connection_remove/', views.api_remove_connection, name="api_remove_connection"),
    url(r'^connection_block/', views.api_block_user, name="api_block_user"),
    url(r'^connection_unblock/', views.api_unblock_user, name="api_unblock_user"),
    url(r'^message_send/', views.api_send_message, name="api_send_message"),
    url(r'^message_received/', views.api_received_messages, name="api_received_messages"),
    url(r'^message_sent/', views.api_sent_messages, name="api_sent_messages"),
]
