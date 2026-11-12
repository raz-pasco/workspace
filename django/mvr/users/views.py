# -*- coding: utf-8 -*-
"""
Created on Sat Mar  07 14:14:03 2026

@author: Pasco
"""

from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
# from .forms import CustomPasswordChangeForm
from django import forms
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('polls:index')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(RegisterView, self).form_valid(form)


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('polls:index')

    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
