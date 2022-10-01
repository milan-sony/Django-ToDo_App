from django import forms
from .models import CustomUser as user

class usersignupform(forms.ModelForm):
  class Meta:
    model = user
    fields = ['name', 'email', 'password']
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form-control',
        # 'placeholder': 'Enter your name',
        # 'required autocomplete': 'off',
      }),
      'email': forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email-input',
        # 'placeholder': 'Enter your Email',
        # 'required autocomplete': 'off',
      }),
      'password': forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'pswd-input',
        # 'placeholder': 'Create your password',
        # 'required autocomplete': 'off',
      }),
    }
  
  # def clean_name(self):
  #   name = self.cleaned_data.get('name')
  #   if(name == ""):
  #     raise forms.ValidationError('This field is required')
  #   return name
  
  # def clean_name(self):
  #   email = self.cleaned_data.get('email')
  #   if(email == ""):
  #     raise forms.ValidationError('This field is required')
  #   return email

  # def clean_name(self):
  #   password = self.cleaned_data.get('password')
  #   if(password == ""):
  #     raise forms.ValidationError('This field is required')
  #   return password
