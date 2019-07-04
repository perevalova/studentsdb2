from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class StProfile(models.Model):
    """To keep extra user data"""

    # user mapping
    user = models.OneToOneField(User)

    class Meta(object):
        verbose_name = _("User Profile")

    # extra user data
    photo = models.ImageField(blank=True, verbose_name=_("Photo"), null=True)
    mobile_phone = models.CharField(max_length=13, blank=True, verbose_name=_("Mobile Phone"), default='')
    passport = models.CharField(max_length=8, blank=True, verbose_name=_("Passport number"))
    city = models.CharField(max_length=20, blank=True, verbose_name=_("City"))
    street = models.CharField(max_length=25, blank=True, verbose_name=_("Street"))
    house = models.CharField(max_length=5, blank=True, verbose_name=_("House"))

    def __str__(self):
        return self.user.username
