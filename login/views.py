from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_login(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('main:home')
        else:
            data = {
                'error': 'Введенные имя пользователя или пароль неверные'
            }
            return render(request, 'login/login.html', data)
    else:
        return render(request, 'login/login.html')


def login_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))