from django.urls import path
from . import views
from .views import index, room_detail,download_excel
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

def home_redirect(request):
    if not request.user.is_authenticated:
        return redirect('login')  # If not logged in, go to login page
    return redirect('index')  # If logged in, go to main page

urlpatterns = [
    path('', home_redirect),  # Redirects to login on first visit
    path('login/', auth_views.LoginView.as_view(template_name='rooms_app/login.html'), name='login'),
    path('index/', index, name='index'),  # Your main dashboard
    path('', index, name='index'),
    path('room/<str:room_number>/', room_detail, name='room_detail'),
    path('room/<str:room_number>/edit/', views.edit_room, name='edit_room'),
    path('tenant/<str:room_number>/edit/', views.edit_tenant, name='edit_tenant'),
    path('download-excel/', download_excel, name='download_excel'),
]

