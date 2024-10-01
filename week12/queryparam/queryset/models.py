from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='tasks')
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50 , choices=[
        ('pending', 'pending'),
        ('complete', 'complete'),
    ])

    def __str__(self):
        return self.name