from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def view_map(request):
    return render(request, 'main/map.html')