from django.shortcuts import render, redirect
# from .models import Secret
from .models import Secret
from ..login_registration.models import User
from django.db.models import Count
from django.contrib import messages

def index(request):
    if not "user_name" in request.session:
        messages.add_message(request, messages.INFO, "Must be logged in to view this page")
        return redirect('login_registration:index')
    context = {
        'secrets': Secret.objects.annotate(num_likes = Count('like')).order_by('-created_at')[:5],
        'logged_user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, "secrets/secrets.html", context)

def create(request):
    if request.method == 'POST':
        secret = Secret.objects.create_secret(request.POST, request.session['user_id'])
        return redirect('secrets:index')

def delete_secret(request):
    if request.method == 'POST':
        Secret.objects.get(id = request.POST['secret_id']).delete()
        return redirect('secrets:index')

def like_secret(request):
    if request.method == 'POST':
        like = Secret.objects.add_like(request.POST)
        return redirect('secrets:index')

def logout(request):
    request.session.clear()
    return redirect('login_registration:index')



# Create your views here.
