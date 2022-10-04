from django import forms
from todolist.models import todolists

class todoform(forms.ModelForm):
  class Meta:
    model = todolists
    fields = ['todo']
    widgets = {
      'todo': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your Tolist here...',
        'required autocomplete': 'off',
      }),
    }
    labels = {
      'todo': 'Add your ToDo'
    }

