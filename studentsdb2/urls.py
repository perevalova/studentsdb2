"""studentsdb2 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import permission_required
from django.urls import path
from django.views.static import serve
from students.views.contact_admin import ContactView
from students.util import lang

from .settings import MEDIA_ROOT
from django.conf import settings

from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog


urlpatterns = i18n_patterns(
    url(r'^lang/(?P<lang_code>[a-z]{2})/$', lang, name='lang'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('', include('students.urls')),
    path('', include('stud_auth.urls')),

    path('', include('social_django.urls', namespace='social')),

    # Contact Admin Form
    path('contact-admin/', permission_required('auth.add_user')(ContactView.as_view()), name='contact_admin'),

    path('admin/', admin.site.urls),

    path('api/v1/', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    # Serve files from media folder
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    ]