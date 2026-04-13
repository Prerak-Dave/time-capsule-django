from django.shortcuts import render
from .forms import UserLogin, UserSignin
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError


def login_user(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        user = authenticate(request, email = request.POST['email'], password = request.POST['password'])
        if user is not None:
            login(request, user)        
    else:
        form = UserLogin()
    
    return render(request, 'tc_auth/login.html', {'form':form})

def signin_user(request):
    if request.method == 'POST':
        form = UserSignin(request.POST)
        if form.is_valid():
            form.save()          
    else:
        form = UserSignin()

    return render(request, 'tc_auth/signin.html', {'form':form})
# Create your views here.