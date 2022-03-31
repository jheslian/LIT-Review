from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
