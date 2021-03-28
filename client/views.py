from django.shortcuts import render,redirect
from .models import Client,Device
from django.views.generic import CreateView
from .forms import DeviceRegistrationForm



class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'phone', 'address', 'client_id']


def DeviceRegistartionView(request):
    if request.method == 'POST':
        form = DeviceRegistrationForm(request.POST)
        if form.is_valid():
            device_id = form.cleaned_data['device_id']
            mac_address = form.cleaned_data['mac_address']
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Your Account Created Successfully! Now you can log in.!')
            device = Device(device_id=device_id,mac_address=mac_address)
            device.save()
            return redirect('register')
    else:

        form = DeviceRegistrationForm()
    return render(request, 'client/device-register.html', {'form': form})