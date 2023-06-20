from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


def name_validator(name):
    if not name.isalpha():
        raise ValidationError('Plant name should consists only letters!')
    return name


class PlantModel(models.Model):
    plant_type = models.CharField(max_length=14, choices=(
        ('Outdoor plants', 'Outdoor plants'),
        ('Indoor plants', 'Indoor plants'),
    ))
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2), name_validator])
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
