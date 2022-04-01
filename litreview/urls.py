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
from app.views import signup_view, login_view, flux, create_review_view, create_ticket_view, follow_view, \
    remove_following_user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('flux/', flux, name='flux'),
    path('ticket/', create_ticket_view, name='create_ticket'),
    path('review/', create_review_view, name='create_review'),
    path('follow/', follow_view, name='follow'),
    path('remove/<int:id>', remove_following_user_view, name='remove_following')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
