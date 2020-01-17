from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import permission_required
from django.urls import path
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog

from students.views.contact_admin import ContactView
from students.util import lang
from .settings import MEDIA_ROOT


urlpatterns = i18n_patterns(
    url(r'^lang/(?P<lang_code>[a-z]{2})/$', lang, name='lang'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('', include('students.urls')),
    path('', include('stud_auth.urls')),

    path('', include('social_django.urls', namespace='social')),

    # Contact Admin Form
    path('contact-admin/', permission_required('auth.add_user')(ContactView.as_view()), name='contact_admin'),

    path('admin/', admin.site.urls),

    # API
    path('api/v1/', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    # Serve files from media folder
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    ]
