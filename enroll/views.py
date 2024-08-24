from django.shortcuts import render , HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data["name"]
            am = fm.cleaned_data["address"]
            em = fm.cleaned_data["email"]
            pm = fm.cleaned_data["password"]
            
            reg = User(name=nm, address=am, email=em, password=pm)
            reg.save()
            
            
            messages.success(request,"sucessfull saved")
            # fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{"form":fm,"stu":stud})

def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()

        return HttpResponseRedirect("/showdata")
    

def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi )
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,"enroll/updatestudent.html",{"form":fm})

def show_data(request):
    stud = User.objects.all()
    return render(request, "enroll/showdata.html",{"stu":stud})

