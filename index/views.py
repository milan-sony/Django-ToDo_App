from django.shortcuts import render,redirect
# from .models import register
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

# Indexpage/Homepage
def index(request):
  return render(request,"index.html")

# UserSignUp
def usersignuppage(request):
  return render(request, "usersignup.html")

# UserLogin
def userloginpage(request):
  return render(request, "userlogin.html")