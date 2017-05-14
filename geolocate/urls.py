from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.geo_locate, name="geo_locate")
]
