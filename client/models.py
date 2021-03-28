from django.db import models
from phone_field import PhoneField
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = PhoneField(blank=True)
    address = models.TextField(primary_key=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('register')