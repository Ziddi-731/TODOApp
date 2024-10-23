from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.core.signals import request_finished
from django.dispatch import receiver,Signal
from home.models import sig



User=get_user_model()
mysignal = Signal()
# Create your views here.
@login_required(login_url='/login/')
def show_todo(request):
    
    mysignal.send(sender=sig,name='ZIDDI')
    if request.method == "GET":
        re=request.user.email
        queryset=Timetable.objects.filter(user__email=re)
    if request.method=="POST":
        title=request.POST.get('title').capitalize()
        desc=request.POST.get('desc')
        usere=request.user.email
        user =request.user
        # print(user.email)
        if title == None or desc == "":
            messages.error(request,"Please Add Title and Description Please!!!")
        else:
            Timetable.objects.create(user=user,title=title,desc=desc)
            messages.success(request,"Todo added successfully!!!")
            queryset=Timetable.objects.filter(user__email=usere)
            return redirect('show_todo')
    
    # queryset=Timetable.objects.filter(user__email=u.email)
    return render(request,"index.html",{'queryset':queryset})
    # return render(request,"index.html")
@login_required(login_url='/login/')
def Delete_todo(request,id):
    print(id)
    q=Timetable.objects.get(id=id)
    q.delete()
    return redirect('show_todo')
@login_required(login_url='/login/')
def update_todo(request,id):
    queryset=Timetable.objects.get(id=id)
    print(queryset.title)
    if request.method=="POST":
        data=request.POST
        title=data.get('title')
        desc=data.get('desc')
        print(title)
        print(desc)
        queryset.title=title
        queryset.desc=desc
        queryset.save()
        return redirect('show_todo')
    context={"queryset":queryset}
    return render(request,"update.html",context)
def Register_page(request):
    
    if request.method=="POST":
        first=request.POST.get('first')
        last=request.POST.get('last')
        email=request.POST.get('email')

        password=request.POST.get('password')
        print(first)
        print(last)
        print(email)
        print(password)
        # print(user.email)
        qE=User.objects.filter(email=email)
        if qE.exists():
            messages.success(request,"Email is already exist!!!!!!")
        else:
            user=User.objects.create(Fist=first,last=last,email=email)
            user.set_password(password)
            user.save()
            messages.info(request,'Account Created!!!!')
            return redirect('/login/')
    return render(request,'register.html')
def login_page(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        if not User.objects.filter(email=email).exists():
            messages.success(request,"Email does not exist!!!!!!!!")
        user=authenticate(email=email,password=password)
        if user == None:
            messages.info(request,"Wrong Password!!!!!")
        else:
            login(request,user)
            return redirect('show_todo')
    return render(request,'login.html')
def logout_page(request):
    logout(request)
    return redirect('/login/')
@receiver(request_finished)
def func(sender,**kwrags):
    print("Request Finished")
# @receiver(mysignal)
# def func2(sender,**kwrags):
#     print("\n\n",kwrags)