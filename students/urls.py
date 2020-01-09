from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path

from students.views.students import StudentList, StudentUpdateView, StudentAddView, StudentDeleteView
from students.views.groups import GroupList, GroupAddView, GroupUpdateView, GroupDeleteView
from students.views.exams import ExamList, ExamAddView, ExamUpdateView, ExamDeleteView
from students.views.journal import JournalView


urlpatterns = [
    path('', StudentList.as_view(), name='home'),
    path('students/add/', login_required(StudentAddView.as_view()), name='students_add'),
    path('students/<int:pk>/edit/', login_required(StudentUpdateView.as_view()), name='students_edit'),
    path('students/<int:pk>/delete/', login_required(StudentDeleteView.as_view()), name='students_delete'),

    # Groups urls
    path('groups/', login_required(GroupList.as_view()), name='groups'),
    path('groups/add/', login_required(GroupAddView.as_view()), name='groups_add'),
    path('groups/<int:pk>/edit/', login_required(GroupUpdateView.as_view()), name='groups_edit'),
    path('groups/<int:pk>/delete/', login_required(GroupDeleteView.as_view()), name='groups_delete'),

    # Visiting urls
    # path('journal/<int:pk>/', login_required(JournalView.as_view()), name='journal'),
    url(r'^journal/(?P<pk>\d+)?/?$', login_required(JournalView.as_view()), name='journal'),

    # Exams urls
    path('exams/', login_required(ExamList.as_view()), name='exams'),
    path('exams/add/', login_required(ExamAddView.as_view()), name='exams_add'),
    path('exams/<int:pk>/edit/', login_required(ExamUpdateView.as_view()), name='exams_edit'),
    path('exams/<int:pk>/delete/', login_required(ExamDeleteView.as_view()), name='exams_delete'),
]