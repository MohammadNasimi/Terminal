from enum import unique
import imp
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# import abstractuser
from django.contrib.auth.models import AbstractUser,UserManager

class Myusermanager(UserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return self._create_user(username, email, password, **extra_fields)
class User(AbstractUser):
   phone = models.CharField( max_length=11,null =True,blank=True,unique=True)
   
   USERNAME_FIELD = 'phone'

   objects =Myusermanager()