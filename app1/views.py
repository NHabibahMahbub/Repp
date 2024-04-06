from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Platform


# Create your views here.
@login_required(login_url='login')
def home(request):
    platform = Platform.objects.all()
    print(platform)
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not (username and email and password1 and password2):
            return HttpResponse("Please fill in all the fields")

        if password1 != password2:
            return HttpResponse("Your password didn't match!")


        else:
            my_user = User.objects.create_user(username, email, password1)
            my_user.save()
            return redirect('home')

    return render(request, 'signup.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password you have given is incorrect. Please try again!")
    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')


def add_platform(request):
    if request.method == "POST":
        form = forms.PlatformForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse("Added Successfully!")
    else:
        form = forms.PlatformForm()
    return render(request, 'forms.html', {
        "form": form
    })


def update_platform(request, p_id):
    p = Platform.objects.get(pk=p_id)
    if request.method == "POST":
        form = forms.PlatformForm(request.POST or None, instance=p)
        if form.is_valid():
            form.save()
            return HttpResponse("Platform is Updated in the page Successfully")
    else:
        form = forms.PlatformForm(instance=p)
    return render(request, 'forms.html', {
        "form": form
    })


def delete_platform(request, p_id):
    Platform.objects.get(pk=p_id).delete()
    return HttpResponse("Platfor is Deleted Successfully")
