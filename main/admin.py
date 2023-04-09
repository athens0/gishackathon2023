from django.contrib import admin
from .models import UAV, Base, Marker


admin.site.register(UAV)
admin.site.register(Base)
admin.site.register(Marker)