from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = 'Create gateway user'

    def handle(self, *args, **kwargs):
        app_name = 'gateway'
        user = User(username=app_name, is_superuser=True)
        user.set_password(app_name)
        user.save()
