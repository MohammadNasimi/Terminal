from enum import unique
import imp
from random import choices
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.db import models

# Create your models here.
# import abstractuser
from django.contrib.auth.models import AbstractUser,UserManager
#validators
from accounts.Validations import validate_phone

class Myusermanager(UserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('type', '1')
        username = extra_fields['phone']
        return self._create_user(username, email, password, **extra_fields)
#### type user 
Choices = ( ('1','Manager'),
             ('2','Driver'),
             ('3','Passenger'))
class User(AbstractUser):
   phone = models.CharField( max_length=11,null =True,blank=True,unique=True,
                            validators=[validate_phone])
   type  = models.CharField(max_length = 2,null = True,blank = True,
                            choices= Choices)
   USERNAME_FIELD = 'phone'

   objects =Myusermanager()