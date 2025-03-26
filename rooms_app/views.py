from django.shortcuts import render
from .models import Room, Tenant
from .forms import RoomForm, TenantForm
from django.shortcuts import render,  redirect
from django.contrib.auth.decorators import login_required



# Create your views here.
# View to show all rooms
@login_required
def index(request):
    #fetch all rooms from database
    rooms = Room.objects.all()
    #store status of each roomm in a dictionary
    room_statuses = {room.room_number: room.status for room in rooms}


    room_numbers = [
        ["100", "102", "104", "105", "106", "107", "108", "109", "110", "111"],
        ["200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "210"],
        ["300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "310"],
    ]    

    return render(request, 'rooms_app/index.html', {
        'room_numbers': room_numbers,
        'room_statuses': room_statuses
        })
#gets all data from database(all rooms), sending them to index, display all rooms on website

# View to show room details
@login_required
def room_detail(request, room_number):
    try:
        room = Room.objects.get(room_number=room_number)
    except Room.DoesNotExist:
        # If room is not found, pass empty data to the template
        room = {
            'room_number': room_number,
            'orientation': 'N/A',
            'window_size': 'N/A',
            'furniture': 'N/A',
            'notes': 'N/A',
            'status': 'Vacant'
        }
    
    tenant = Tenant.objects.filter(room__room_number=room_number).first()
    if not tenant:
        tenant = {
            'first_name': 'N/A',
            'middle_name': 'N/A',
            'last_name': 'N/A',
            'nick_name': 'N/A',
            'checkin_date': 'N/A',
            'payment_due_date': 'N/A',
            'parking_spot': 'N/A'
        }

    return render(request, 'rooms_app/room.html', {'room': room, 'tenant':tenant})
#fetching data of specific room from database, showing them on room.html page

@login_required
def edit_room(request, room_number):
    # Fetch the room, but without unpacking as a tuple
    room = Room.objects.get_or_create(
        room_number=room_number,
        defaults={
            'orientation': 'N/A',
            'window_size': 'N/A',
            'furniture': 'N/A',
            'notes': 'N/A',
            'status': 'Vacant'
        }
    )[0]  # 👈 Get only the first element (the room object)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_detail', room_number=room_number)
    else:
        form = RoomForm(instance=room)

    return render(request, 'rooms_app/edit.html', {'form': form, 'room_number': room_number})

@login_required
def edit_tenant(request, room_number):
    room = Room.objects.get_or_create(
        room_number=room_number,
        defaults={
            'orientation': 'N/A',
            'window_size': 'N/A',
            'furniture': 'N/A',
            'notes': 'N/A',
            'status': 'Vacant'
        }
    )[0]

    tenant = Tenant.objects.get_or_create(
        room=room,  # Assuming a OneToOne or ForeignKey relationship
        defaults={
            'first_name': 'N/A',
            'middle_name': 'N/A',
            'last_name': 'N/A',
            'nick_name': 'N/A',
            'checkin_date': None,
            'payment_due_date': None,
            'parking_spot': False
        }
    )[0]

    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect('room_detail', room_number=room_number)
    else:
        form = TenantForm(instance=tenant)

    return render(request, 'rooms_app/edit.html', {'form': form, 'room_number': room_number, 'edit_type': 'tenant'})



#FOR CONVERTING TO EXCEL
import pandas as pd
from django.http import HttpResponse
from django.db import connection

def download_excel(request):
    with connection.cursor() as cursor:
        # Fetch data from Table 1
        cursor.execute("SELECT * FROM rooms_app_room")  # Replace with your table name
        columns1 = [col[0] for col in cursor.description]
        rows1 = cursor.fetchall()
        df1 = pd.DataFrame(rows1, columns=columns1)

        # Fetch data from Table 2
        cursor.execute("SELECT * FROM rooms_app_tenant")  # Replace with your table name
        columns2 = [col[0] for col in cursor.description]
        rows2 = cursor.fetchall()
        df2 = pd.DataFrame(rows2, columns=columns2)

    # Create HTTP response for Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Raysidence_database.xlsx'

    # Write both tables to separate sheets in the Excel file
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df1.to_excel(writer, sheet_name='Room_Details', index=False)
        df2.to_excel(writer, sheet_name='Tenant_Information', index=False)

    return response