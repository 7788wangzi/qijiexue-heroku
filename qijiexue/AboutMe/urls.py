"""
Definition of urls for AboutMe.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from Resume import views


    #path('', views.home, name='home'),
    
   # path('', include('profile.urls')),

urlpatterns = [    
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('gallery/', views.gallery, name='gallery'),
    path('projects/', views.projects, name='projects'),
    path('animation/', views.animation, name='animation'),
]
