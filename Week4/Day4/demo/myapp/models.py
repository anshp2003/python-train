from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=30,null=True,blank=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name