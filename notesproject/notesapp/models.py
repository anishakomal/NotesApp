from django.db import models


from datetime import datetime

class Note(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
          