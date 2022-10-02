from django.db import models

from user.models import CustomUser

# Create your models here.
class todolists(models.Model):
  status_choices = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
  ]
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  todo = models.CharField(max_length = 50)
  status = models.CharField(max_length=1, choices=status_choices, default=status_choices[1]) 
  # A new migration is created each time the order of choices changes
  created_date = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = "todolist"
    verbose_name_plural = "todolists"
    db_table = 'todolists'