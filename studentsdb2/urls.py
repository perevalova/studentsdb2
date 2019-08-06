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
from django.views.static import serve
from students.views.contact_admin import ContactView
from students.util import lang

from .settings import MEDIA_ROOT, DEBUG

from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog


urlpatterns = i18n_patterns(
    url(r'^lang/(?P<lang_code>[a-z]{2})/$', lang, name='lang'),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^', include('students.urls')),
    url(r'^', include('stud_auth.urls')),

    url('', include('social_django.urls', namespace='social')),

    # Contact Admin Form
    url(r'^contact-admin/$', permission_required('auth.add_user')(ContactView.as_view()), name='contact_admin'),

    url(r'^admin/', admin.site.urls),
)

if DEBUG:
    # Serve files from media folder
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    ]
