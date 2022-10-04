from django.urls import path,include
from . import views

urlpatterns = [
  path('userhome_todo/', views.userhome_todo, name='userhome_todo'),
  path('addtodolist/', views.addtodolist, name='addtodolist'),
  path('status_update/<int:id>', views.status_update, name='status_update'),
  path('delete_todo/<int:id>', views.delete_todo, name='delete_todo'),
  path('edit_todo/<int:id>', views.edit_todo, name='edit_todo'),
]