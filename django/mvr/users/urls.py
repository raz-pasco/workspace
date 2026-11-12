# -*- coding: utf-8 -*-
"""
Created on Sat Mar  07 14:17:03 2026

@author: Pasco
"""
from django.urls import path
from .views import RegisterView, MyLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('login/', MyLoginView.as_view(),name='login'),
]
