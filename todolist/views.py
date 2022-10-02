from django.shortcuts import redirect, render
from django.contrib import messages
from todolist.forms import todoform
from todolist.models import todolists

# Create your views here.

def userhome_todo(request):
  form = todoform()
  if request.user.is_authenticated:
    user = request.user
    todolist = todolists.objects.filter(user = user)
    return render(request, "userhomepage.html", {'todoform':form, 'todolist':todolist})

def addtodolist(request):
  if request.user.is_authenticated:
    user = request.user
    print(user)
    form = todoform(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
      todolist = form.save(commit=False) 
      # Saving with commit=False gets you a model object, then you can add your extra data and save it
      # https://stackoverflow.com/questions/12848605/django-modelform-what-is-savecommit-false-used-for
      todolist.user = user
      todolist.save()
      print(todolist)
      messages.warning(request, "Your list is added")
      return redirect('todolist:userhome_todo')
    else:
      messages.warning(request, "Something went wrong please try again")
      return redirect('todolist:userhome_todo')

