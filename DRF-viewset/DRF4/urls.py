"""DRF4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from api import views
from rest_framework.routers import DefaultRouter

#creating router object

router = DefaultRouter()
#registring viewset with router

# router.register('oneforall', views.StudentViewset,basename='one')

router.register('oneforall', views.StudentModelViewset,basename='one')
# router.register('oneforall', views.StudentROModelViewset,basename='one')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    #need to add for session authentication for below code
    path('auth/',include('rest_framework.urls')),

    #function based urls
    # path('api_view',views.web_api_test),
    # path('api_view/<int:pk>',views.web_api_test),
]
