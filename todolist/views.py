from django.shortcuts import render
from todolist.forms import todoform
# Create your views here.
def userhome_todo(request):
  form = todoform()
  return render(request, "userhomepage.html", {'todoform':form})
  
