from django.core.management.base import BaseCommand
from rooms_app.reminders.tasks import payment_reminder

class Command(BaseCommand):
    help = "Send monthly payment reminders to admin"

    def handle(self, *args, **kwargs):
        payment_reminder()
        self.stdout.write(self.style.SUCCESS('Successfully sent reminders.'))