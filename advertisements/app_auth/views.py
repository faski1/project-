from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url=reverse_lazy('profile'))
def profile(request):
    return render(request, 'app_auth/profile.html')

def login(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
      if  request.user.is_authenticated:
          return redirect(redirect_url)
      else:
          return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {"error" : "Пользователь на найден"})

def logout(request):
    logout(request)
    return redirect(reverse('login'))
