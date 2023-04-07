from django.shortcuts import render

def layout(request):
    return render(request, 'main/layout.html')

def index(request):
    return render(request, 'main/index.html')

def header(request):
    return render(request, 'main/header.html')

def footer(request):
    return render(request, 'main/footer.html')