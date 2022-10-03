from django.core.exceptions import ValidationError

def validate_phone(value : str) :
    if  not value.startswith("09") :
        raise ValidationError(
            ('you should start with 09 '),
            params={'value': value},
        )
    if  len(value)!=11:
        raise ValidationError(
            ('size equal 11 example: 09141231213'),
            params={'value': value},
        )