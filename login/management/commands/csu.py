from django.core.management import BaseCommand
from login.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(email="admin@exsample.com")
        user.set_password("password")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
