from django.conf.urls import url
import views

urlpatterns = [
    url(r'^profile/', views.other_profile, name="other_profile"),
    url(r'^connections/', views.user_connections, name="user_connections"),
    url(r'^invitations/', views.user_connections, name="user_connections"),
    url(r'^blocked/', views.user_connections, name="user_connections"),
    url(r'^connections_json/', views.api_user_connections, name="api_user_connections"),    
]
