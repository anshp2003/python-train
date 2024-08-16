from django.db import models
from django.utils import timezone

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)  # Automatically set to the current date when created

    def __str__(self):
        return self.title
