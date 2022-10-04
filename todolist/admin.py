from django.contrib import admin

from todolist.models import todolists

# Register your models here.
class usertodolist(admin.ModelAdmin) :
  list_display = ('user', 'todo', 'created_date')
  search_fields = ('todo',) # Without the comma, ('user') is the same as 'user', which is a string, not a tuple.
  #https://stackoverflow.com/questions/31765584/django-admin-error-admin-e008-the-value-of-fieldsets-must-be-a-list-or-tuple

admin.site.register(todolists, usertodolist)