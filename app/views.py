from django.shortcuts import render, redirect
from .forms import SignupForm
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        print("1",request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("2")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print("us", user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                return redirect('flux')

            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe est invalid.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe est invalid.")

    return render(request, 'app/login.html', context={'form': form})


def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte est créé.")
            return redirect(settings.LOGIN_URL)
    return render(request, 'app/signup.html', context={'form': form})

