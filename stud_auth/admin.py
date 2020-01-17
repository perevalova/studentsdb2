from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import User

from .models import StProfile


class StProfileInline(admin.StackedInline):
    model = StProfile
    fields = ['avatar_tag','photo', 'mobile_phone', 'passport', 'city', 'street', 'house']
    readonly_fields = ['avatar_tag']


class UserAdmin(auth_admin.UserAdmin):
    inlines = (StProfileInline,)
    list_display = ('avatar_tag',) + auth_admin.UserAdmin.list_display

    def avatar_tag(self, obj):
        return obj.stprofile.avatar_tag()

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
