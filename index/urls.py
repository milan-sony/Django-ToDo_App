from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.usersignup, name='usersignup'),
    path('login', views.userlogin, name='userlogin'),
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