from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from .models import User
from .forms import RegisterUser

from django.http import HttpResponse
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)

def home(request):
    return render(request,'accounts/home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'User is successfully created with username:- {username}')
            return redirect(reverse('accounts:home'))
        form = RegisterUser(request.POST)
        return render(request, 'accounts/register.html', {'form': form})
    form = RegisterUser()
    return render(request, 'accounts/register.html', {'form': form})

#
class PasswordChange(PasswordChangeView):
    template_name = 'accounts/passwordchange.html'
    success_url = reverse_lazy('accounts:password_change_done')


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/passwordchangedone.html'
