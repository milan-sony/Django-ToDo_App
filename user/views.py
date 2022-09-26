from django.shortcuts import render,redirect
from .models import CustomUser as user
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

#! User signup
def usersignup(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST.get('password')
    confirmpassword = request.POST.get('confirmpassword')

    if password == confirmpassword:
      if user.objects.filter(email=email).exists():
        messages.warning(request, "This Email is already exist")
        return redirect('usersignuppage')
      else:
        user(name=name, email=email, password=password).save()
        messages.success(request, "Your accout has been successfully created")
        return redirect('userloginpage')
    else:
      messages.warning(request, "Password is not matching")
      return redirect('usersignuppage')

  return render(request, "usersignup.html")

#! User login

def userlogin(request):
  pass
