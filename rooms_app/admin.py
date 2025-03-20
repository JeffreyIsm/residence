from django.contrib import admin

# Register your models here.
from .models import Room #This is the class we just created in models.py
admin.site.register(Room)

from .models import Tenant
admin.site.register(Tenant)