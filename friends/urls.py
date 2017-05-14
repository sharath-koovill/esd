from django.conf.urls import url
import views

urlpatterns = [

    url(r'^$',
       views.list_friends,
       name='friends_friends'),

    url(r'^invite/(?P<username>[\.\w]+)/$',
       views.invite_friend,
       name='friends_invite'),

    url(r'^remove/(?P<username>[\.\w]+)/$',
       views.remove_friend,
       name='friends_remove'),

    url(r'^block/(?P<username>[\.\w]+)/$',
       views.block_user,
       name='friends_block_user'),

    url(r'^unblock/(?P<username>[\.\w]+)/$',
       views.unblock_user,
       name='friends_unblock_user'),

    url(r'^blocked/$',
       views.list_blocked_users,
       name='friends_blocked_users'),

    url(r'^invitations/received/$',
       views.list_received_invitations,
       name='friends_received_invitations'),

    url(r'^invitations/sent/$',
       views.list_sent_invitations,
       name='friends_sent_invitations'),

    url(r'^invitation/(?P<invitation_id>[\d]+)/$',
       views.show_invitation,
       name='friends_show_invitation'),

    url(r'^invitation/(?P<invitation_id>[\d]+)/remove/$',
       views.remove_invitation,
       name='friends_remove_invitation'),

    url(r'^invitation/(?P<invitation_id>[\d]+)/accept/$',
       views.respond_to_invitation,
       {'resp': 'a'},
       name='friends_accept_invitation'),

    url(r'^invitation/(?P<invitation_id>[\d]+)/decline/$',
       views.respond_to_invitation,
       {'resp': 'd'},
       name='friends_decline_invitation'),

    url(r'^of_friend/(?P<username>[\.\w]+)/$',
        views.list_friend_friends,
        name='friends_friend_friends'),


]

