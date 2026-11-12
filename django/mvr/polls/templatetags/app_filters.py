# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 04:54:03 2026

@author: Pasco
"""
from django import template
from num2words import num2words

register = template.Library()

@register.filter
# """
# * ``cardinal`` (default)
# * ``ordinal``
# * ``ordinal_num``
# * ``year``
# * ``currency``
# """
def number_to_words(value, lang='en', to='ordinal'):
    try:
        return num2words(value, lang=lang, to=to)
    except Exception as e:
        print(f"Error converting number to words:{e}")

