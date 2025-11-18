from django.urls import path

# importing views from views.py
from .views import NoteListCreateAPIView


urlpatterns = [
    path("notes/", NoteListCreateAPIView.as_view()),
]

