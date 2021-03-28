from django.shortcuts import render, redirect
from .models import Client, Device
from django.views.generic import CreateView
from .forms import DeviceRegistrationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class ClientCreateView(SuccessMessageMixin, CreateView):
    model = Client
    success_message = 'Client successful created'
    fields = ['name', 'email', 'phone', 'address', 'client_id']


def DeviceRegistartionView(request):
    if request.method == 'POST':
        form = DeviceRegistrationForm(request.POST)
        if form.is_valid():
            device_id = form.cleaned_data['device_id']
            mac_address = form.cleaned_data['mac_address']
            messages.success(request, f'Device {device_id} registered successfully.!')
            device = Device(device_id=device_id, mac_address=mac_address)
            device.save()
            return redirect('device-entry')
    else:

        form = DeviceRegistrationForm()
    return render(request, 'client/device-register.html', {'form': form})
