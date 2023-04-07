from django.shortcuts import render


def login_main(request):
    return render(request, 'login/login.html')