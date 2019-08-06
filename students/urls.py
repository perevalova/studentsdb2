from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from students.views.students import StudentList, StudentUpdateView, StudentAddView, StudentDeleteView
from students.views.groups import GroupList, GroupAddView, GroupUpdateView, GroupDeleteView
from students.views.exams import ExamList, ExamAddView, ExamUpdateView, ExamDeleteView
from students.views.journal import JournalView


urlpatterns = [
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
]