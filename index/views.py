from django.shortcuts import render

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