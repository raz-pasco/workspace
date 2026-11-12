# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 16:18:03 2025

@author: Pasco
"""

from django.contrib import admin

# Register your models here.
from .models import Choice, Question

"""class ChoiceInline(admin.StackedInline):"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    search_fields = ["question_text"]
    list_filter = ["pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    inlines = [ChoiceInline]
    """
    fields = ["pub_date", "question_text"]
    """

"""admin.site.register(Choice)"""
admin.site.register(Question, QuestionAdmin)
