from django.shortcuts import render, redirect
from .models import UAV, Base

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
    print(request.user.groups)
    if request.user.groups.filter(name='диспетчеры').exists():
        data = dict()
        base = Base.objects.filter(disp_id=request.user.id)[0]
        uavs = UAV.objects.filter(base_id=base.id)
        data['uavs'] = uavs
        data['base'] = base
        return render(request, 'main/sub-disp.html', data)
    if request.user.groups.filter(name='операторы').exists():
        return render(request, 'main/sub-oper.html')
    return redirect(request.META.get('HTTP_REFERER', '/'))