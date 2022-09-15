import email
from django.db import models

# Create your models here.
class user(models.Model):
  name = models.CharField(max_length=50, null=False)
  email = models.EmailField(unique=True)
  password1 = models.CharField(max_length=50, null=False)
  password2 = models.CharField(max_length=50, null=False)

  class Meta:
    db_table = 'user'