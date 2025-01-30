from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name='programming')

