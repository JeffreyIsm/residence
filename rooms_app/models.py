from django.db import models

# Create your models here.
class Room(models.Model):
    WINDOW_CHOICES = [
        ('normal', 'Normal'),
        ('small', 'Small'),
    ]

    STATUS_CHOICES = [
        ('occupied', 'Occupied'),
        ('occupiedpark', 'OccupiedPark'),
        ('vacant', 'Vacant'),
        ('unused', 'Unused'),
        ('others', 'Others'),
    ]

    room_number = models.CharField(max_length=10,blank=True, null=True)
    orientation = models.CharField(max_length=10,blank=True, null=True)
    window_size = models.CharField(max_length=10, choices=WINDOW_CHOICES,blank=True,null=True)
    furniture = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES,blank=True, null=True)

    def __str__(self):
        return f"Room {self.room_number}"
    
class Tenant(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100,blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    checkin_date = models.DateField(null=True, blank=True)
    payment_due_date = models.PositiveSmallIntegerField(null=True, blank=True)
    parking_spot = models.BooleanField(default=False,blank=True, null=True)

    def __str__(self):
        return self.first_name + '' + self.last_name
    
    def save(self, *args, **kwargs):
        if self.room:
            if self.parking_spot:
                self.room.status = 'occupiedpark'
            else:
                self.room.status = 'occupied'
            self.room.save()
        super().save(*args, **kwargs)