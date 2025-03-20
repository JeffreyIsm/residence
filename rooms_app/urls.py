from django.urls import path
from . import views
from .views import index, room_detail, tenant_detail,download_excel

urlpatterns = [
    path('', index, name='index'),
    path('room/<str:room_number>/', room_detail, name='room_detail'),
    path('room/<str:room_number>/edit/', views.edit_room, name='edit_room'),
    path('tenant/<str:room_number>/', tenant_detail, name='tenant_detail'),
    path('tenant/<str:room_number>/edit/', views.edit_tenant, name='edit_tenant'),
    path('download-excel/', download_excel, name='download_excel'),
]

