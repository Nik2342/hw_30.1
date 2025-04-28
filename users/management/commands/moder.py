from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        moderator_group = Group.objects.create(name="Moder")
        user = User.objects.create(email="moder@moder.com")
        user.set_password("moder")
        user.save()
        user.groups.add(moderator_group)
