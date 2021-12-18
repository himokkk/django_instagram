from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .forms import RegisterForm
from main.models import Profile

# Create your views here.

def register(response):
    if str(response.user) != 'AnonymousUser':
        return HttpResponseRedirect('/login')  
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            obj = Profile.objects.create(user=user)
            obj.save()
            return redirect("/login")
        return redirect("/register")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})