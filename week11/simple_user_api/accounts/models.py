from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    phonenumber = models.IntegerField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.username


class recepie(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)


class Ingredient(models.Model):
    Ingredient_name=models.CharField(max_length=50)
    Ingredient_qnt=models.CharField(max_length=50)
    recepie_name=models.ForeignKey(recepie,related_name="ingredients",on_delete=models.CASCADE,blank=True,null=True)

    

class Instruction(models.Model):
    no_of_step=models.IntegerField()
    description_of_step=models.CharField(max_length=500)
    recepie_name=models.ForeignKey(recepie,related_name="instructions",on_delete=models.CASCADE,blank=True,null=True)
