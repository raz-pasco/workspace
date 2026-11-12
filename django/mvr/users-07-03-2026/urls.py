# -*- coding: utf-8 -*-
"""
Created on Sun Nov  10 09:40:03 2025

@author: Pasco
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]
