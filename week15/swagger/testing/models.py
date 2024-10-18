from django.db import models

# Create your models here.

class CustomUser(models.Model):
    name = models.CharField(max_length=50)



class Address(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(CustomUser, related_name='addresses',blank=True, on_delete=models.CASCADE)




class PhoneNumber(models.Model):
    number = models.CharField(max_length=50)
    user_id = models.ForeignKey(CustomUser, blank=True,related_name='phonenumbers', on_delete=models.CASCADE)

       
