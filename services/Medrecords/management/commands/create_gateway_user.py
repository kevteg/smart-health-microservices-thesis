from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = 'Create gateway user'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        groups = Group.objects.all()
        print(users[0].groups.all())

