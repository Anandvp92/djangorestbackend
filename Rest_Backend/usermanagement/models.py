from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.


class User(AbstractBaseUser):
    email=models.EmailField(verbose_name="Email",max_length=30)
    phonenumber=models.CharField(verbose_name="Phone Number",max_length=10,min_length=10)