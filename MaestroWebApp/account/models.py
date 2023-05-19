from django.db import models
from django.core.validators import MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=128, validators=[MinLengthValidator(8)])
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
