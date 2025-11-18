from django.shortcuts import render

from django.http import HttpResponse
from .models import Note
from .serializers import NoteSerializer
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView



class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
