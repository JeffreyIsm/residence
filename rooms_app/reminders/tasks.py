from datetime import date
from django.core.mail import send_mail
from rooms_app.models import Tenant
from django.conf import settings

def payment_reminder():
    today = date.today().day
    tenant_due_today = Tenant.objects.filter(payment_due_date=today)

    for T in tenant_due_today:
        full_name = f"{T.first_name} {T.last_name}"
        room_number = T.room.room_number if T.room else "N/A"

        send_mail(
            subject="Payment Reminder",
            message=(
                f"Hello,\n\nThis is a reminder that {full_name} "
                f"(Room {room_number}) has rent due today ({today}).\n\n"
                f"Peace out,\n"
                f"Lebron James"
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["tulodongbawah111@gmail.com"],
            fail_silently=False,
        )