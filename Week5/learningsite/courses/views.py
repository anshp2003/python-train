from django.shortcuts import render
from .models import Course
# Create your views here.
def home(request):
    obj=Course.objects.all()
    return render(request,'index.html',{"data":obj})