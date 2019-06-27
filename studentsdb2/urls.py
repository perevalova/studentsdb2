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
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import RedirectView
from django.views.static import serve
from students.views.contact_admin import ContactView
from students.views.students import StudentList, StudentUpdateView, StudentAddView, StudentDeleteView
from students.views.groups import GroupList, GroupAddView, GroupUpdateView, GroupDeleteView
from students.views.exams import ExamList, ExamAddView, ExamUpdateView, ExamDeleteView
from students.views.journal import JournalView
from students.util import lang

from .settings import MEDIA_ROOT, DEBUG
from students.views import students, groups, journal, exams, contact_admin

from django.utils.translation import ugettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
from django.contrib.auth import views as auth_views


# urlpatterns = (
#     url(r'^i18n/', include('django.conf.urls.i18n')),
#     #url(r'^setlang/$', set_language, name='set_language'),
#     #url(r'^$', StudentList.as_view(), name='home'),
#
# )

urlpatterns = i18n_patterns(
    url(r'^lang/(?P<lang_code>[a-z]{2})/$', lang, name='lang'),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^$', StudentList.as_view(), name='home'),
    url(r'^students/add/$', login_required(StudentAddView.as_view()), name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', login_required(StudentUpdateView.as_view()), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', login_required(StudentDeleteView.as_view()), name='students_delete'),

    # Groups urls
    url(r'^groups/$', login_required(GroupList.as_view()), name='groups'),
    url(r'^groups/add/$', login_required(GroupAddView.as_view()), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', login_required(GroupUpdateView.as_view()), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', login_required(GroupDeleteView.as_view()), name='groups_delete'),

    # Visiting urls
    url(r'^journal/(?P<pk>\d+)?/?$', login_required(JournalView.as_view()), name='journal'),

    # Exams urls
    url(r'^exams/$', login_required(ExamList.as_view()), name='exams'),
    url(r'^exams/add/$', login_required(ExamAddView.as_view()), name='exams_add'),
    url(r'^exams/(?P<pk>\d+)/edit/$', login_required(ExamUpdateView.as_view()), name='exams_edit'),
    url(r'^exams/(?P<pk>\d+)/delete/$', login_required(ExamDeleteView.as_view()), name='exams_delete'),

    # Contact Admin Form
    url(r'^contact-admin/$', permission_required(ContactView.as_view()), name='contact_admin'),

    url(r'^admin/', admin.site.urls),

    # User Related urls
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)


if DEBUG:
    # Serve files from media folder
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    ]
