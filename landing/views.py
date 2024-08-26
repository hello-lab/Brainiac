from urllib.parse import urlencode
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .forms import RegisterUser, LoginUser
from .models import User
import uuid
from dashboard.views import home_page

# Create your views here.
def landing_page(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            try: 
                loggedin = User.objects.get(name=name, password=password)
                print(loggedin.id)
                request.session["member_logged_id"] = int(loggedin.id)
                return redirect((f'/admin/'))
            except Exception as e:
                print(e)
                request.session["error_message"] = "Invalid Credentials"
                return redirect((f'/admin/404/'))
    else:
        form = LoginUser()
    return render(request, 'login.html', {
        'form': form
    })

def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            try: 
                User.objects.create(**form.cleaned_data)
                return redirect((f'/login/'))
            except Exception as e:
                print(e)
                request.session["error_message"] = e
                return redirect((f'/admin/404/'))
            # name = User.objects.get(email=form.cleaned_data['email']).name
            
    else:
        form = RegisterUser()

    return render(request, 'register.html', {
        'form': form
    })
