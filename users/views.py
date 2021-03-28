from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User Account, {username} Created Successfully!')
            return redirect('register')
    else:

        form = RegistrationForm
    return render(request, 'users/register.html', {'form': form})
