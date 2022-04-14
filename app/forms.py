from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Ticket, Review
from django import forms


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username"]


class TicketForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["headline", "rating", "body"]
