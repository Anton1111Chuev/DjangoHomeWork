from django.core.management.base import BaseCommand
from mainapp.models import User


class Command(BaseCommand):
    help = "Add user."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('phone_number', type=str, help='User phone number')
        parser.add_argument('address', type=str, help='User address')

    def handle(self, *args, **kwargs):
        user = User(name=kwargs.get('name'),
                    email=kwargs.get('email'),
                    phone_number=kwargs.get('phone_number'),
                    address=kwargs.get('address')
                    )
        user.save()
        self.stdout.write(f'{user}')
