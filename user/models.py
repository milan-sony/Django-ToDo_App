from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import datetime, timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.

#! Creating custom user model with AbstractUser
# Reference link about AbstractUser:
# https://testdriven.io/blog/django-custom-user-model/
# https://stackoverflow.com/questions/21514354/difference-between-abstractuser-and-abstractbaseuser-in-django

class CustomUser(AbstractBaseUser, PermissionsMixin):
  name = models.CharField(max_length=150)
  email = models.EmailField(unique=True)
  date_joined = models.DateTimeField(default=datetime.now())
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  def __str__(self):
    return self.email

  class Meta:
    verbose_name = "user"
    verbose_name_plural = "users"
    db_table = 'accounts'
  #   abstract = True
  # In this case, (inside AbstractBaseUser) it is defined as abstract = True
  # If abstract = True, this model will be an abstract  base class