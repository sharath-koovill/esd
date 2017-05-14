"""classifieds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from sevalinks.views import home, sevalinks_404, sevalinks_500

handler404 = 'sevalinks.views.sevalinks_404'
handler500 = 'sevalinks.views.sevalinks_500'
#handler403 = 'sevalinks.views.my_custom_permission_denied_view'
#handler400 = 'sevalinks.views.my_custom_bad_request_view'

urlpatterns = [
	url(r'^geo/', include('geolocate.urls')),
    url(r'^seva/', include('sevalinks.urls')),
    url(r'^contacts/', include('contacts.urls')),    
    url(r'^admin/', admin.site.urls),
    url(r'^404/', sevalinks_404, name='sevalinks_404'), 
    url(r'^500/', sevalinks_500, name='sevalinks_500'), 
    url(r'^$', home, name='home'),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
