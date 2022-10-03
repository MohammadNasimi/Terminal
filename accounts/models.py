from django.db import models
from django.apps import apps

# Create your models here.
# import abstractuser
from django.contrib.auth.models import AbstractUser,UserManager
from django.contrib.auth.hashers import make_password

#validators
from accounts.Validations import validate_phone,validate_birthday

class Myusermanager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
            """
            Create and save a user with the given username, email, and password.
            """
            if not username:
                raise ValueError('The given username must be set')
            email = self.normalize_email(email)
            # Lookup the real model class from the global app registry so this
            # manager method can be used in migrations. This is fine because
            # managers are by definition working on the real model.
            GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
            username = GlobalUserModel.normalize_username(username)
            user = self.model(username=username, email=email, **extra_fields)
            user.password = make_password(password)
            user.save(using=self._db)
            Manager.objects.create(user =user)
            return user
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
   
   

class profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

class Manager(profile):
    pass
    def __str__(self) -> str:
        return f'{self.user.phone ,self.user.type}'
    
class Driver(profile):
    Certificatenumber = models.CharField(max_length=15)
    def __str__(self) -> str:
        return f'{self.user.phone ,self.user.type}'
    
class Passenger(profile):
    nationalcode = models.CharField(max_length=15)
    birthday = models.DateTimeField(null =True,validators =[validate_birthday])
    accountbalance = models.PositiveIntegerField()
    
    def get_ticket(self,price):
        self.accountbalance = self.accountbalance - price
        return self.accountbalance
    
    
    def __str__(self) -> str:
        return f'{self.user.phone ,self.user.type}'
