from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
