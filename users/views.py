from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth import get_user_model

from .form import *


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title' : 'Авторизация'}



class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileForm
    template_name = 'users/profile.html'
    extra_context = {'title' : 'Профиль пользователя'}

    def get_success_url(self):
        return reverse_lazy('users:profile')
    
    def get_object(self,queryset = None):
        return self.request.user



class RegisterUser(CreateView):
    form_class = RegistrationUserForm
    template_name = 'users/registration.html'
    extra_context = {'title' : 'Регистрация'}
    success_url = reverse_lazy('users:login')


class UserPasswordChange(PasswordChangeView):
    form_class = PasswordChangeUserForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change_form.html'

