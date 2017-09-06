from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, "login_registration/index.html")

def register(request):
    result = User.objects.validate_and_register(request.POST)
    if result[0] == False:
        context = {
            'result':result[1]
        }
        return render(request, "login_registration/index.html", context)
    if result[0] == True:
        context = {
            'user_name': result[1],
            'action': "successfully registered!"
        }
        return render(request, "login_registration/index.html", context)

def login(request):
    result = User.objects.validate_and_login(request.POST)
    if result[0] == False:
        context = {
            'result':result[1]
        }
        return render(request, "login_registration/index.html", context)
    if result[0] == True:
        request.session['user_name'] = result[1][0].first_name
        request.session['user_id'] = result[1][0].id
        return redirect('/secrets')

# Create your views here.
