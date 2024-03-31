

from django.urls import path, reverse, include
from .views import dashboard, CustomLoginView, logout_view, profile, registration
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout_view, name='logout'),
]