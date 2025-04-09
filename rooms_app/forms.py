from django import forms
from .models import Room, Tenant

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['orientation', 'window_size', 'furniture', 'notes', 'status']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Exclude 'occupiedpark' from the status dropdown
        self.fields['status'].choices = [
            choice for choice in self.fields['status'].choices if choice[0] != 'occupiedpark'
        ]

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['first_name', 'middle_name', 'last_name', 'nick_name', 'checkin_date', 'payment_due_date', 'parking_spot']
        widgets = {
            'checkin_date': forms.DateInput(attrs={'type': 'date'}),
            'payment_due_date': forms.NumberInput(attrs={'min': 1, 'max': 31}),
        }
