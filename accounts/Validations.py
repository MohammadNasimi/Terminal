import imp
from django.core.exceptions import ValidationError
import datetime
def validate_phone(value : str) :
    if  not value.startswith("09") :
        raise ValidationError(
            ('you should start with 09 '),
            params={'value': value},
        )
    if  len(value)!=11 or not value.isnumeric():
        raise ValidationError(
            ('size equal 11 example: 09141231213'),
            params={'value': value},
        )
        
def validate_birthday(value):
    if  datetime.datetime.now().year - value.year > 15:
        raise ValidationError(
            ('you should older than 15 '),
            params={'value': value},
        )
    if  datetime.datetime.now().year > value.year :
        raise ValidationError(
            ('less today time'),
            params={'value': value},
        )
        
def validate_password(pas1,pas2):
    if pas1 != pas2:
        raise ValidationError(
            ('password must match'),
            params={'value': pas1},
        )