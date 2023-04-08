from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('map/', views.view_map, name='map'),
    path('about/', views.about_us, name='about'),
    path('jobs/', views.jobs, name='jobs'),
    path('sub/', views.sub, name='sub')
]
