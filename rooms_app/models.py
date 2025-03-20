from django.db import models

# Create your models here.
class Room(models.Model):
    WINDOW_CHOICES = [
        ('normal', 'Normal'),
        ('small', 'Small'),
    ]

    STATUS_CHOICES = [
        ('occupied', 'Occupied'),
        ('vacant', 'Vacant'),
        ('unused', 'Unused'),
        ('others', 'Others'),
    ]

    room_number = models.CharField(max_length=10)
    orientation = models.CharField(max_length=10)
    window_size = models.CharField(max_length=10, choices=WINDOW_CHOICES,blank=True,null=True)
    furniture = models.TextField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Room {self.room_number}"
    
class Tenant(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    checkin_date = models.DateField(null=True, blank=True)
    payment_due_date = models.DateField(null=True, blank=True)
    parking_spot = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + '' + self.last_name