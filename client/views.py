from django.shortcuts import render
from .models import Client
from django.views.generic import CreateView


class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'phone', 'address']