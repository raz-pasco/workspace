# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:17:03 2025

@author: Pasco
"""

from django.urls import include, path
from . import views

# We need to make precion to the app name
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
