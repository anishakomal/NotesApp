from django.db import models
from django.utils import timezone

from datetime import datetime


class Note(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
