from django.forms import ModelForm
from todolist.models import todolists

class todoform(ModelForm):
  class Meta:
    model = todolists
    fields = ['todolist', 'status']
