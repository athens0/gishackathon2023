from django.shortcuts import render, redirect

def index(request):
    return render(request, 'main/index.html')

def view_map(request):
    return render(request, 'main/map.html')

def about_us(request):
    return render(request, 'main/about.html')

def jobs(request):
    return render(request, 'main/jobs.html')

def sub(request):
    if not request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'main/sub.html')