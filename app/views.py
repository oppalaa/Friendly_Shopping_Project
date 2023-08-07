from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def registration(request):
    d={'usfo':UserForm(),'pfo':ProfileForm()}
    if request.method=='POST' and request.FILES:
        usfd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if usfd.is_valid() and pfd.is_valid():
            NSUFO=usfd.save(commit=False)
            submittedPassword=usfd.cleaned_data['password']
            NSUFO.set_password(submittedPassword)
            NSUFO.save()
            NSPO=pfd.save(commit=False)
            NSPO.username=NSUFO
            NSPO.save()
            
            
            send_mail('registartion',
                      'registration is sucessful in Friendly Shopping ',
                      'oppalanaveen143@gmail.com',
                      [NSUFO.email],
                      fail_silently=False )
            return HttpResponse('registration form is successful check in admin')        
    return render(request,'registration.html',d)


def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Not a Active User')
        else:
            return HttpResponse('Invalid Details')
    return render(request,'user_login.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def display_details(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=Profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'display_details.html',d)


@login_required
def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('password was changed')
    return render(request,'change_password.html')

def reset_password(request):
    if request.method=='POST':
        password=request.POST['pw']
        username=request.POST['un']
        LUO=User.objects.filter(username=username)
        if LUO:
            UO=LUO[0]
            UO.set_password(password)
            UO.save()
            return HttpResponse('reset_password is done')
        else:
            return HttpResponse('invalid data')
    return render(request,'reset_password.html')


def Mens_Wear(request):
    return render(request,'Mens_Wear.html')


def Womens_Wear(request):
    return render(request,'Womens_Wear.html')

def Kids_Wear(request):
    return render(request,'Kids_Wear.html')

def mobiles(request):
    return render(request,'mobiles.html')

def electronics(request):
    return render(request,'electronics.html')

def Friendly_Tv(request):
    return render(request,'Friendly_Tv.html')

def Homee(request):
    return render(request,'Homee.html')

def web_series(request):
    return render(request,'web_series.html')

def short_films(request):
    return render(request,'short_films.html')

def comedy(request):
    return render(request,'comedy.html')
