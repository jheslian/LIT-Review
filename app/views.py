from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, TicketForm, ReviewForm
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserFollows, Ticket, Review
from itertools import chain
from django.db.models import Q
from django.db.utils import IntegrityError


# Create your views here.


def login_view(request):
    """ Login user """
    form = AuthenticationForm()
    if request.user.is_authenticated:
        return redirect("flux")
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                return redirect("flux")

            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe est invalid.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe est invalid.")

    return render(request, "app/login.html", context={"form": form})


def signup_view(request):
    """ Create user account """
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte est créé.")
            return redirect(settings.LOGIN_URL)
    return render(request, "app/signup.html", context={"form": form})


@login_required
def flux(request):
    """ Main page - The tickets and reviews of the user itself and user the user follows """
    users_followers = UserFollows.objects.filter(user=request.user)
    users = []
    for user in users_followers:
        users.append(user.followed_user)
    tickets = Ticket.objects.filter(Q(has_review=False) & (Q(user=request.user) | Q(user__in=users)))
    reviews = Review.objects.filter(Q(user=request.user) | Q(user__in=users))

    tickets_and_reviews = sorted(chain(tickets, reviews), key=lambda obj: obj.time_created, reverse=True)
    return render(request, "app/flux.html", context={"content": tickets_and_reviews})


@login_required
def create_ticket_and_review_view(request):
    """ Create ticket and review at the same time. """
    ticket_form = TicketForm()
    review_form = ReviewForm()

    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.has_review = True
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.ticket.has_review = True
            review.user = request.user
            review.save()
            messages.success(request, "Le ticket et le critique sont créés.")
            return redirect("posts")

    context = {"ticket_form": ticket_form, "review_form": review_form}

    return render(request, "app/create_ticket_review.html", context=context)


@login_required
def create_ticket_view(request):
    """ Create a ticket """
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, "Votre ticket est créé.")
            return redirect("posts")
    context = {"form": form}
    return render(request, "app/create_ticket.html", context=context)


@login_required
def follow_users_view(request):
    """ Follow a user and get user followers """
    following_users = UserFollows.objects.filter(user=request.user.id)
    users_followers = UserFollows.objects.filter(followed_user=request.user.id)
    if request.POST:
        user = User.objects.get(username=request.POST["following"])

        if str(request.user) == request.POST["following"]:
            messages.error(request, "Vous ne pouvez pas suivre vous même")
            return redirect("follow")

        try:
            form = UserFollows()
            form.user = request.user
            form.followed_user = user
            form.save()
            messages.success(
                request, f"Vous avez bien ajouté {request.POST['following']} sur votre reseau.",
            )
        except IntegrityError:
            messages.error(request, f"Vous suivez déjà {user}")

        return redirect("follow")

    context = {"following": following_users, "followers": users_followers}
    return render(request, "app/follow.html", context=context)


@login_required
def remove_following_user_view(request, id):
    """ Remove a follower """
    user = get_object_or_404(User, id=id)
    remove_user = UserFollows.objects.get(user=request.user.id, followed_user=user)
    remove_user.delete()
    return redirect("follow")


@login_required
def posts_view(request):
    """ Get tickets and reviews for the post page"""
    tickets = Ticket.objects.filter(Q(user=request.user))
    reviews = Review.objects.filter(Q(user=request.user))

    tickets_and_reviews = sorted(chain(tickets, reviews), key=lambda obj: obj.time_created, reverse=True)

    return render(request, "app/posts.html", context={"tickets_and_reviews": tickets_and_reviews})


@login_required
def update_ticket(request, id):
    """ Update a user ticket """
    context = {}
    ticket = get_object_or_404(Ticket, id=int(id))
    context["form"] = TicketForm(instance=ticket)
    if request.method == "POST":
        update_form = TicketForm(request.POST, request.FILES, instance=ticket)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, "Votre ticket est modifié.")
            return redirect("posts")

    context["ticket"] = ticket

    return render(request, "app/update_ticket.html", context=context)


@login_required
def update_review(request, review_id):
    """ Update a user review"""
    context = {}
    review = get_object_or_404(Review, id=review_id)
    context["form"] = ReviewForm(instance=review)
    if request.method == "POST":
        update_form = ReviewForm(request.POST, instance=review)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, "Votre ticket est modifié.")
            return redirect("posts")

    context["review"] = review

    return render(request, "app/update_review.html", context=context)


@login_required
def create_review(request, ticket_id):
    """ Create a review of a ticket """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if ticket.has_review:
        messages.error(request, "Ce ticket à déjà une critique.")
        return redirect("posts")
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            ticket.has_review = True
            ticket.save()
            messages.success(request, "Votre critique est crée.")
            return redirect("posts")

    context = {"ticket": ticket, "form": form}

    return render(request, "app/create_review.html", context=context)


@login_required
def delete_ticket(request, ticket_id):
    """ Delete user ticket """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    messages.success(request, f"Votre ticket {ticket.title} est bien supprimé.")
    return redirect("posts")


@login_required
def delete_review(request, review_id):
    """ Delete user review """
    review = get_object_or_404(Review, id=review_id)
    ticket = get_object_or_404(Ticket, id=review.ticket.id)
    ticket.has_review = False
    ticket.save()
    review.delete()
    messages.success(request, f"Votre critique {review.headline} est bien supprimé.")
    return redirect("posts")
