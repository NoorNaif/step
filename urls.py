from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='home-page'),
    path('registerView',views.registerView,name='register'),
    #path('profileView',views.profileView,name='profile'),
]
