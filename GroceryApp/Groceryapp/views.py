from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,AnonymousUser
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from .models import Items

def index(request):
    ur = request.user.username
    items = Items.objects.all()
    return render(request, 'index.html',{'uname':ur,'items':items})

def cartView(request):
    return render(request,'cart.html')

def SignupPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if(p1!=p2):
            return HttpResponse("Your passwords does not matched please re-enter")
        my_user = User.objects.create_user(uname,email,p1)
        my_user.save()
        return redirect('login')
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if(user is not None):
            login(request,user)
            items = Items.objects.all()
            return render(request,'index.html',{'uname':user,'items':items})
        else:
            return HttpResponse("user not found please create an account")
    return render(request, 'login.html')


def add_to_cart(request,id):
    name = request.GET.get('name')
    item = Items.objects.get(id=id)
    user = request.user
    return HttpResponseRedirect(request.path_info)
