from django.db import models

# Create your models here.
class MenuItems(models.Model):
    name = models.CharField(max_length=128)
    size = models.CharField(max_length=5, choices=[
        ('150', '150G'),
        ('200', '200G')
    ], default='150G')
    price = models.IntegerField()
