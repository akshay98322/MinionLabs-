from django.db import models
from phone_field import PhoneField
from django.urls import reverse


class Device(models.Model):
    device_id = models.CharField(max_length=20, blank=False)
    mac_address = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.device_id


class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = PhoneField(blank=True)
    address = models.TextField(primary_key=True)
    client_id = models.ForeignKey(Device,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client-create')



