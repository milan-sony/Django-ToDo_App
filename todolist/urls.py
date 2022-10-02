from django.urls import path,include
from . import views

app_name = 'todolist'

urlpatterns = [
  path('userhome_todo', views.userhome_todo, name='userhome_todo'),
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name = 'index'),
#     path('valueinsert/',views.valueinsert, name = 'valueinsert'),
#     path('viewlist/', views.viewlist, name = 'viewlist'),
#     path('update/<int:id>',views.update),
#     path('delete/<int:id>',views.delete),
#     path('search/',views.search, name = 'search')
# ]