from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Ticket, Review
from django import forms
from django.utils.translation import gettext as _


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
