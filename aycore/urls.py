"""mow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static  # new

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
    
    #path('cms/', include(wagtailadmin_urls)),
    #path('documents/', include(wagtaildocs_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', include('aydashboard.urls')),
    path('', include('ayregistration.urls')),
    #path('', include(wagtail_urls)),  
   

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# refer to https://docs.wagtail.io/en/v2.11.2/advanced_topics/add_to_django_project.html
