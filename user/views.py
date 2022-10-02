from django.shortcuts import render,redirect
from user.models import CustomUser as user
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from todolist.forms import todoform

# Create your views here.

#! User signup
def usersignup(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    confirmpassword = request.POST['confirmpassword']

    if password == confirmpassword:
      if user.objects.filter(email=email).exists():
        messages.warning(request, "User with this Email already exist")
        return redirect('usersignuppage')
      else:
        user(name=name, email=email, password=make_password(password)).save() # make_password is used to make the password into hashed/encrypted format
        messages.success(request, "Your accout has been successfully created")
        return redirect('userloginpage')
    else:
      messages.warning(request, "password fields didn't match.")
      return redirect('usersignuppage')

  return render(request, "usersignup.html")

#! User login
def userlogin(request):
  # form = todoform()
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
      login(request, user)
      return redirect('userhome_todo')
      # return render(request, "userhomepage.html", {'todoform':form})
    else:
      messages.warning(request, "Check you username and password")
      return redirect('userlogin')
  else:
    return render(request, "userlogin.html")
