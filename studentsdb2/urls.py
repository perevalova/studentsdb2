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
from django.views.static import serve
from students.views.contact_admin import ContactView
from students.views.students import StudentUpdateView, StudentAddView, StudentDeleteView
from students.views.groups import GroupAddView, GroupUpdateView, GroupDeleteView
from students.views.exams import ExamAddView, ExamUpdateView, ExamDeleteView

from .settings import MEDIA_ROOT, DEBUG
from students.views import students, groups, journal, exams, contact_admin

urlpatterns = [
    #Students urls
    url(r'^$', students.students_list, name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^students/add/$', StudentAddView.as_view(), name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

    # Groups urls
    url(r'^groups/$', groups.groups_list, name='groups'),
    url(r'^groups/add/$', GroupAddView.as_view(), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='groups_delete'),

    # Visiting urls
    url(r'^journal/$', journal.students_visiting, name='journal'),
    #url(r'^journal/(?P<vid>\d+)/edit/$', journal.students_edit, name='students_edit'),

    # Exams urls
    url(r'^exams/$', exams.exams_list, name='exams'),
    url(r'^exams/add/$', ExamAddView.as_view(), name='exams_add'),
    url(r'^exams/(?P<pk>\d+)/edit/$', ExamAddView.as_view(), name='exams_edit'),
    url(r'^exams/(?P<pk>\d+)/delete/$', ExamAddView.as_view(), name='exams_delete'),

    # Contact Admin Form
    url(r'^contact-admin/$', ContactView.as_view(), name='contact_admin'),

    url(r'^admin/', admin.site.urls),
]


if DEBUG:
    # Serve files from media folder
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    ]
