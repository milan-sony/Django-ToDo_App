from django.shortcuts import render,redirect
# from .models import register
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

# Indexpage/Homepage
def index(request):
  return render(request,"index.html")