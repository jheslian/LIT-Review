"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from app.views import signup_view, login_view, flux, create_ticket_view, create_ticket_and_review_view, follow_users_view, \
    remove_following_user_view, posts_view, update_ticket, update_review


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('flux/', flux, name='flux'),
    path('ticket/create/', create_ticket_and_review_view, name='create_ticket_review'),
    path('review/create/', create_ticket_view, name='create_ticket'),
    path('follow/', follow_users_view, name='follow'),
    path('remove/<int:id>', remove_following_user_view, name='remove_following'),
    path('posts/', posts_view, name='posts'),
    path('ticket/<int:ticket_id>/update', update_ticket, name='update_ticket'),
    path('review/<int:ticket_id>/update', update_review, name='update_review'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
