from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UAV, Base, Marker

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
        markers = Marker.objects.all()
        uavs_front = []
        markers_front = []
        for uav in uavs:
            current = [uav.img_url, uav.name, uav.on_flight, User.objects.filter(id=uav.oper_id)[0].username, uav.max_range, uav.cord_x, uav.cord_y, uav.destination, uav.duration, uav.id]
            uavs_front.append(current)
        for mk in markers:
            current = [mk.id, mk.name, mk.uav_id, mk.description, mk.state, mk.marker, mk.cord_x, mk.cord_y]
            markers_front.append(current)
        data['uavs'] = uavs_front
        data['base'] = base
        data['markers'] = markers_front
        data['map'] = 'https://static-maps.yandex.ru/1.x/?ll=111.126512,63.424022&size=650,450&z=7&l=map&pt='
        for base in Base.objects.all():
            data['map'] += f'{base.cord_x},{base.cord_y},pm2bl~'
        for uav in UAV.objects.all():
            data['map'] += f'{uav.cord_x},{uav.cord_y},pm2wtm{uav.id}~'
        for marker in Marker.objects.all():
            data['map'] += f'{marker.cord_x},{marker.cord_y},'
            if marker.state == 0:
                data['map'] += f'pm2orm{marker.id}~'
            elif marker.state == 1:
                data['map'] += f'pm2grm{marker.id}~'
            else:
                data['map'] += f'pm2rdm{marker.id}~'
        data['map'] = data['map'][:-1]
        print(data['map'])
        return render(request, 'main/sub-disp.html', data)
    if request.user.groups.filter(name='операторы').exists():
        return render(request, 'main/sub-oper.html')
    return redirect(request.META.get('HTTP_REFERER', '/'))