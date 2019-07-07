from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from students.models import Student, Group

from django.utils.translation import ugettext as _


class Command(BaseCommand):
    help = _('Prints to console number of students, groups and users related objects in a database.')
    models = (('student', Student), ('group', Group), ('user', User))

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(_('student'), help='<model_name model_name ...>')
        parser.add_argument(_('group'), help='<model_name model_name ...>')
        parser.add_argument(_('user'), help='<model_name model_name ...>')

    def handle(self, *args, **options):
        for name, model in self.models:
            if name in options:
                self.stdout.write(_('Number of %(var)ss in database: %(modelname)d', dict(var=name, modelname=model.objects.count())))
            else:
                raise CommandError()
