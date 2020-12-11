from django.contrib import admin
from django.urls import path
from .views import LoginView, LogoutView, UserRegistration, PasswordChangeView, PasswordResetView, \
    PasswordResetSet, PasswordResetDone
from django.contrib.auth import views as django_auth

app_name = 'authentication'
urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("signup/", UserRegistration.as_view(), name='signup'),

    #path('password_reset/done'),
# TODO: add password_change view link to profile page
    path("password_change", PasswordChangeView.as_view(), name='password-change'),

    path("password_reset/", PasswordResetView.as_view(), name='password-reset'),
    path("password_reset_set/", PasswordResetSet.as_view(), name='password-reset-set'),
    path("password_reset_done/", PasswordResetDone.as_view(), name='password-reset-done'),
]