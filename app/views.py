from django.shortcuts import render, redirect
from .forms import SignupForm, TicketForm, ReviewForm
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_view(request):
    form = AuthenticationForm()
    if request.user.is_authenticated:
        return redirect('flux')
    if request.method == 'POST':
        print("1", request.POST)
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


@login_required
def flux(request):
    return render(request, 'app/flux.html', context={})


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
            print("z", ticket, review)
            messages.success(request, "Votre ticket et le critique sont créés.")
            return redirect('create_review')

    context = {
        'ticket_form': ticket_form,
        'review_form': review_form
    }

    return render(request, 'app/create_review.html', context=context)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class RestrictedView(LoginRequiredMixin, TemplateView):
    template_name = 'foo/restricted.html'
    raise_exception = True
    permission_denied_message = "Access interdit."
