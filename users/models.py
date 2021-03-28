from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from django.db import models


class CustomUser(AbstractUser):
    phone = PhoneField(blank=True, help_text='Contact phone number')
