from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _


def upload_to(instance, filename):
    return 'avatars/%s' % filename


class StProfile(models.Model):
    """To keep extra user data"""

    # user mapping
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta(object):
        verbose_name = _("User Profile")

    # extra user data
    photo = models.ImageField(blank=True, upload_to=upload_to, verbose_name=_("Photo"), null=True)
    mobile_phone = models.CharField(max_length=13, blank=True, verbose_name=_("Mobile Phone"), default='')
    passport = models.CharField(max_length=8, blank=True, verbose_name=_("Passport number"))
    city = models.CharField(max_length=20, blank=True, verbose_name=_("City"))
    street = models.CharField(max_length=25, blank=True, verbose_name=_("Street"))
    house = models.CharField(max_length=5, blank=True, verbose_name=_("House"))

    def __str__(self):
        return self.user.username

    def get_photo(self):
        if not self.photo:
            return static('img/default_user.png')
        return self.photo.url

    # method for creating a fake field of a table in read only mode
    def avatar_tag(self):
        return mark_safe(
            '<img src="%s" width="50" height="50" />' % self.get_photo())

    avatar_tag.short_description = _("Avatar")
