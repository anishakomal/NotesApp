from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Note

import datetime


def note(request):
    now = datetime.datetime.now()
    return HttpResponse(now)


def get_notes(request):
    notes = Note.objects.all()
