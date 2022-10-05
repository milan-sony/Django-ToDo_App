from django.urls import path
from . import views

urlpatterns = [
    path('usersignup/', views.usersignup, name='usersignup'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),
]