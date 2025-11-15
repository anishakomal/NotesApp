from django.urls import path

# importing views from views.py
from .views import note

urlpatterns = [
    path('',note),
]
