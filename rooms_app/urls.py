from django.urls import path
from . import views
from .views import index, room_detail,download_excel
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),  # Your main dashboard
    path('login/', auth_views.LoginView.as_view(template_name='rooms_app/login.html'), name='login'),
    path('room/<str:room_number>/', room_detail, name='room_detail'),
    path('room/<str:room_number>/edit/', views.edit_room, name='edit_room'),
    path('tenant/<str:room_number>/edit/', views.edit_tenant, name='edit_tenant'),
    path('download-excel/', download_excel, name='download_excel'),
]

