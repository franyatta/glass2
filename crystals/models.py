from django.db import models
from django.utils import timezone

class Crystal(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(help_text="Age in hours")
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name