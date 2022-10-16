from django.db import models
from user.models import CustomUser
from django_cryptography.fields import encrypt
# https://github.com/georgemarshall/django-cryptography
# https://pypi.org/project/django-cryptography/

# Create your models here.
class todolists(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  todo = encrypt(models.CharField(max_length=255))
  todo_completed = models.BooleanField(default=False)
  created_date = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.user.email
  # This is used to change the adminside object name

  class Meta:
    verbose_name = "todolist"
    verbose_name_plural = "todolists"
    db_table = 'todolists'