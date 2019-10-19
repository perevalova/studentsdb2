from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StudAuthConfig(AppConfig):
    name = 'stud_auth'
    verbose_name = _("Student authorization")
