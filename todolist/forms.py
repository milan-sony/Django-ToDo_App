from django import forms
from todolist.models import todolists

class todoform(forms.ModelForm):
  class Meta:
    model = todolists
    fields = ['todo']
    widgets = {
      'todo': forms.TextInput(attrs={
        'class': 'form-control',
        # 'placeholder': 'Enter your name',
        # 'required autocomplete': 'off',
      }),
    }

