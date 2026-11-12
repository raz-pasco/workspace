# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:17:03 2025

@author: Pasco
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from num2words import num2words
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.db.models import F
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# Create your views here.
#from django_password_eye.fields import PasswordEye

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['num_visits'] = self.request.session['num_visits']
        return data

    def get(self, request):
        num_visits = self.request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        return super().get(request)


    def get_queryset(self):
        """return the last five published question"""
        return  Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
        """return Question.objects.order_by("-pub_date")[:5]"""

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['num_visits'] = self.request.session['num_visits']
        return data

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['num_visits'] = self.request.session['num_visits']
        return data



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selectet_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice."
            }
        )
    else:
        selectet_choice.votes = F("votes") + 1
        selectet_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
