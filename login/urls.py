from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login_login, name='login'),
    path('logout/', views.login_logout, name='logout')
]