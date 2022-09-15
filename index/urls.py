from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
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