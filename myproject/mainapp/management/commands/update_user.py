from django.core.management.base import BaseCommand
from mainapp.models import User


class Command(BaseCommand):
    help = "Update user."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='pk User')
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('phone_number', type=str, help='User phone number')
        parser.add_argument('address', type=str, help='User address')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user:
            user.name=kwargs.get('name'),
            user.email=kwargs.get('email'),
            user.phone_number=kwargs.get('phone_number'),
            user.address=kwargs.get('address')
            user.save()
        self.stdout.write(f'{user}')
