from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import datetime

def note(request):
    now = datetime.datetime.now()
    return HttpResponse(now)