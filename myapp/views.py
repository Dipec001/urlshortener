from django.shortcuts import render, redirect
from django.http import JsonResponse
import string
import random
from .models import UrlShortener
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        base_url = base_url = request.build_absolute_uri('/')[:-1]  # Get the base URL dynamically
        long_url = request.POST['url']
        if long_url:
            short_id = generate_short_id()
            short_url = f"{base_url}/{short_id}"

            url = UrlShortener(long_url=long_url, short_id=short_id, short_url=short_url)
            url.save()
            return JsonResponse({'status':'success', 'data':{'short_url':short_url}})
        else:
            return JsonResponse({'error':'Please pass the url you want to shorten'})

    return render(request,'index.html')

def generate_short_id():
    # initializing size of string
    N = 8
    
    # using random.choices()
    # generating random strings
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
    #return string
    return (str(res))

def redirect_long_url(request, short_id):
    url = UrlShortener.objects.get(short_id=short_id)
    if url:
        return redirect(url.long_url)
    return JsonResponse({'error':'The url doesn\'t exist'})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'})

            # If username is unique, create the user
            user = User(username=username)
            user.set_password(password)
            user.save()
            return redirect('home')
        else:
            return JsonResponse({'error': 'All fields are required'})
    
    return render(request, 'register.html')

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return JsonResponse({'error':'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')