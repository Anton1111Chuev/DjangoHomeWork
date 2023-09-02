from django.core.management.base import BaseCommand
from mainapp.models import User


class Command(BaseCommand):
    help = "list user."

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')