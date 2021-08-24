from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

# Create your models here.
