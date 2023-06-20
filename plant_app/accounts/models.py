from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def name_validator(name):
    if not name[0].isalpha() or not name[0].isupper():
        raise ValidationError('Your name must start with capital letter!')
    else:
        return name


class ProfileModel(models.Model):
    username = models.CharField(max_length=10, null=True, validators=[MinLengthValidator(2)])
    first_name = models.CharField(max_length=30, null=True, blank=False, validators=[name_validator])
    last_name = models.CharField(max_length=30, null=True, blank=False, validators=[name_validator])
    profile_picture = models.URLField(null=True, blank=False)
