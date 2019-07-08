import random
from datetime import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string

from students.models import Student, Group


class Command(BaseCommand):
    help = 'Create random users, student, groups'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            random_number = random.randint(1000, 6000)

            User.objects.create_user(username=get_random_string(), email='', password='123')
            Student.objects.create(first_name=get_random_string(), last_name=get_random_string(), birthday=datetime.now(), ticket=random_number, student_group_id=2)
            Group.objects.create(title=get_random_string(length=5))