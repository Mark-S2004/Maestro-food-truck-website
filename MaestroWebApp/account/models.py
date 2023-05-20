import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    OriginalB = models.PositiveSmallIntegerField(default=0)
    OriginalC = models.PositiveSmallIntegerField(default=0)
    ChiliB = models.PositiveSmallIntegerField(default=0)
    ViolaB = models.PositiveSmallIntegerField(default=0)
    HardRockB = models.PositiveSmallIntegerField(default=0)
    MaestroB = models.PositiveSmallIntegerField(default=0)
    BeethovenB = models.PositiveSmallIntegerField(default=0)
    RanchC = models.PositiveSmallIntegerField(default=0)
    SticksC = models.PositiveSmallIntegerField(default=0)
    StripsC = models.PositiveSmallIntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = uuid.uuid4().hex[:30]
        super().save(*args, **kwargs)
