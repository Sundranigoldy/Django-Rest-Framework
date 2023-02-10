"""DRF3 URL Configuration

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
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #function based view

    # path('api_view',views.web_api_test),
    # path('api_view/<int:pk>',views.web_api_test),
    # for web_api_test

    #class based view
    # path('api_view',views.StudentAPI.as_view()),
    # path('api_view/<int:pk>',views.StudentAPI.as_view()),
    
    
    
    
    #generic view..

    path('api_view',views.LCStudent.as_view()),
    # path('api_view',views.StudentCreate.as_view()),
    # path('api_view/<int:pk>',views.StudentRetrive.as_view()),
    # path('api_view/<int:pk>',views.StudentUpdate.as_view()),
    # path('api_view/<int:pk>',views.RUDStudent.as_view()),

    #for concrete view
    # path('api_view/<int:pk>',views.RUStudent.as_view()),
    path('api_view/<int:pk>',views.RudStudent.as_view()),

]
