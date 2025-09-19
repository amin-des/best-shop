from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField(unique=True)
    # phone_activation_code = models.IntegerField()
    # email_activation_code = models.CharField()
    def __str__(self):
        return self.username



