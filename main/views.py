from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about_us(request):
    return render(request, 'main/about.html')

def jobs(request):
    return render(request, 'main/jobs.html')