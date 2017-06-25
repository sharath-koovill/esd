from django.conf.urls import url
import views
import views_account

urlpatterns = [
	url(r'^notification_check/', views_account.api_notification_check, name="api_notification_check"),
	url(r'^notification_ack/', views_account.api_notification_ack, name="api_notification_ack"),
	url(r'^subscriptions/', views.user_subscriptions, name="user_subscriptions"),
	url(r'^changeimage/', views.change_image_render, name="change_image_render"),
	url(r'^confirmrequest/', views.confirm_render, name="confirm_render"),
	url(r'^confirmsuccess/', views.confirm_success, name="confirm_success"),
	url(r'^forgotpassword/', views.forgot_password, name="forgot_password"),
	url(r'^resetpassword/', views.reset_password, name="reset_password"),
	url(r'^changepassword/', views.change_password, name="change_password"),
	url(r'^resetrequestsuccess/', views.reset_password_request, name="reset_password_request"),
	url(r'^addlocation/', views_account.add_location, name="add_location"),
	url(r'^addprofession/', views_account.add_profession, name="add_profession"),
	url(r'^addimage/', views_account.add_image, name="add_image"),
	url(r'^userhome/', views_account.user_landing, name="user_landing"),
	url(r'^landing/', views_account.user_landing, name="user_landing"),
	url(r'^find/', views_account.user_find, name="user_find"),
	url(r'^editprofilerender/', views.edit_profile_render, name="edit_profile_render"),
	url(r'^editprofile/', views.edit_profile, name="edit_profile"),
	url(r'^myaccount/', views.user_account, name="user_account"),
	url(r'^register/', views.user_register, name="user_register"),
	url(r'^login/', views.user_login, name="user_login"),
	url(r'^logout/', views.user_logout, name="user_logout"),
	url(r'^$', views.home, name='home'),
]
