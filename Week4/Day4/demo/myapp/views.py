from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import user

# Create your views here.
def home(request):
    return render(request,'index.html')

def form(request):
    
    if request.method=="POST":
        a=request.POST.get("nm")
        b=request.POST.get("em")
        c=request.POST.get("ps")
        obj=user(name=a,email=b,password=c)
        obj.save()
        users=user.objects.all()
        return render(request,'success.html',{'user': users})
    return render(request,'form.html')

def delete_form_data(request, id):
    form_data = get_object_or_404(user, id=id)
    form_data.delete()
    users=user.objects.all()
    return render(request,'success.html',{'user': users})
    