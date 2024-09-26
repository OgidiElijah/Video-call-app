
from django.shortcuts import render,redirect

from .forms import userRegisterForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def home(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['email']
            messages.success(request, f'Account created for {username}! login.')
            return redirect('login')
    else: 

        form = userRegisterForm()
    return render(request, 'home.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged in as {email}')
            return redirect('/index/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    messages.success(request, 'You have logged out successfully')
    return redirect('home')