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
from django.views.generic.base import TemplateView
from django.views.static import serve
from students.views.contact_admin import ContactView
from students.views.students import StudentList, StudentUpdateView, StudentAddView, StudentDeleteView
from students.views.groups import GroupList, GroupAddView, GroupUpdateView, GroupDeleteView
from students.views.exams import ExamList, ExamAddView, ExamUpdateView, ExamDeleteView
from students.views.journal import JournalView
from students.util import lang
from stud_auth.views import UserView
from students.views.users import UserList

from .settings import MEDIA_ROOT, DEBUG

from django.utils.translation import ugettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
from django.contrib.auth import views as auth_views


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
    url(r'^contact-admin/$', permission_required('auth.add_user')(ContactView.as_view()), name='contact_admin'),

    url('', include('social_django.urls', namespace='social')),
    url(r'^users/$', UserList.as_view(), name='users'),

    url(r'^admin/', admin.site.urls),

    # User Related urls
    url(r'^accounts/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    url(r'^accounts/profile/(?P<pk>\d+)/$', login_required(UserView.as_view()), name='user'),
    url(r'^accounts/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)


if DEBUG:
    # Serve files from media folder
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    ]
