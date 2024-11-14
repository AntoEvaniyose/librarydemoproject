from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# CustomUser Definition

class CustomUser(AbstractUser):
    address=models.CharField(max_length=20,default="")
    phone=models.IntegerField(default=0)

    is_superuser=models.BooleanField(default=False)     #admin user
    is_user=models.BooleanField(default=False)          #normal user

    def __str__(self):
        return self.username


class Users(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    email=models.CharField(max_length=20)

    def __str__(self):
        return self.name
