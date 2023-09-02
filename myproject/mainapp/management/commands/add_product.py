from django.core.management.base import BaseCommand
from mainapp.models import Product


class Command(BaseCommand):
    help = "Add product."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('quantity', type=int, help='Product quantity')

    def handle(self, *args, **kwargs):
        product = Product(name=kwargs.get('name'),
                          description=kwargs.get('description'),
                          price=kwargs.get('price'),
                          quantity=kwargs.get('quantity')
                          )
        product.save()
        self.stdout.write(f'{product}')
