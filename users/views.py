from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Your Account Created Successfully! Now you can log in.!')
            return redirect('register')
    else:

        form = RegistrationForm
    return render(request, 'users/register.html', {'form': form})
