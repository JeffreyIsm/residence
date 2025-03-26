from django import forms
from .models import Room, Tenant

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['orientation', 'window_size', 'furniture', 'notes', 'status']

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['first_name', 'middle_name', 'last_name', 'nick_name', 'checkin_date', 'payment_due_date', 'parking_spot']
        widgets = {
            'checkin_date': forms.DateInput(attrs={'type': 'date'}),
            'payment_due_date': forms.NumberInput(attrs={'min': 1, 'max': 31}),
        }
