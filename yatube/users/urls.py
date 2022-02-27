# users/urls.py

# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/',
         auth_views.PasswordChangeView.
         as_view(), name='password_reset_form'
         ),
]
