from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, TicketForm, ReviewForm
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserFollows, Ticket, Review


# Create your views here.

def login_view(request):
    form = AuthenticationForm()
    if request.user.is_authenticated:
        return redirect('flux')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
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


@login_required
def flux(request):
    return render(request, 'app/flux.html', context={})


@login_required
def create_ticket_view(request):
    form = TicketForm()

    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, "Votre ticket est créé.")
            return redirect('create_ticket')
    return render(request, 'app/create_ticket.html', context={'form': form})


@login_required
def create_review_view(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()

    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            messages.success(request, "Votre ticket et le critique sont créés.")
            return redirect('create_review')

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form
    }

    return render(request, 'app/create_review.html', context=context)


@login_required
def follow_view(request):
    following_users = UserFollows.objects.filter(user=request.user.id)
    users_followers = UserFollows.objects.filter(followed_user=request.user.id)

    if request.POST:
        form = UserFollows()
        user_follow = User.objects.get(username=request.POST['following'])
        form.user = request.user
        form.followed_user = user_follow
        form.save()
        return redirect('follow')

    context = {'following': following_users, 'followers': users_followers}
    return render(request, 'app/follow.html', context=context)


def remove_following_user_view(request, id):

    user = get_object_or_404(User, id=id)
    remove_user = UserFollows.objects.get(user=request.user.id ,followed_user=user)
    remove_user.delete()
    return redirect('follow')
