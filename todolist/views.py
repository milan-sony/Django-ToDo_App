from django.shortcuts import redirect, render
from django.contrib import messages
from todolist.models import todolists

# Create your views here.

# User home
def userhome_todo(request):
  if request.user.is_authenticated:
    user = request.user
    todolist = todolists.objects.filter(user = user)
    return render(request, "userhomepage.html", {'todolist':todolist})
  else:
    return render(request, "404.html")

# Add todolist
def addtodolist(request):
  if request.method == 'POST':
    todo = request.POST['todo']
    todolist = todolists(user=request.user, todo=todo)
    todolist.save()
    messages.success(request, "New list is added")
    return redirect('userhome_todo')
  else:
    messages.warning(request, "Something went wrong please try again")
    return redirect('userhome_todo')

# Edit todolist
def edit_todo(request, id):
  todolist = todolists.objects.get(id=id)
  if request.method == 'POST':
    newtodo = request.POST['newtodo']
    todolist.todo = newtodo
    todolist.save()
    messages.success(request, "Todolist updated")
    return redirect('userhome_todo')
  else:
    return render(request, "edit_todolist.html",{'todolist':todolist}) 

# Update status of todolist
def status_update(request, id):
  todolist = todolists.objects.get(id=id)
  current_status = todolist.todo_completed
  todolist.todo_completed = not current_status 
  todolist.save()
  return redirect('userhome_todo') 

# Delete todolist
def delete_todo(request, id):
  todolist = todolists.objects.get(id=id)
  if request.method == 'POST':
    todolist.delete()
    messages.success(request, "Todolist deleted")
    return redirect('userhome_todo')
  else:
    return render(request, "confirm_delete.html",{'todolist':todolist}) 
