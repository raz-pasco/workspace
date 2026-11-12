#!/bin/bash
. storage/django/venv/bin/activate 
cd storage/django/sigpo
python manage.py runserver
