from django.conf.urls import url
from django.contrib.auth.decorators import permission_required

from .views import StudentList, StudentDetail, GroupList, GroupDetail, ExamList, \
    ExamDetail, JournalList, JournalDetail, ContactView

urlpatterns = [
    url(r'^students/$', StudentList.as_view(), name='students'),
    url(r'^students/(?P<pk>\d+)/$', StudentDetail.as_view(), name='students_detail'),

    # Groups urls
    url(r'^groups/$', GroupList.as_view(), name='groups'),
    url(r'^groups/(?P<pk>\d+)/$', GroupDetail.as_view(), name='groups_detail'),

    # Visiting urls
    url(r'^journal/$', JournalList.as_view(), name='journal'),
    url(r'^journal/(?P<pk>\d+)?/?$', JournalDetail.as_view(), name='journal_detail'),

    # Exams urls
    url(r'^exams/$', ExamList.as_view(), name='exams'),
    url(r'^exams/(?P<pk>\d+)/$', ExamDetail.as_view(), name='exams_detail'),

    url(r'^contact-admin/$', permission_required('auth.add_user')(ContactView.as_view()),
        name='contact_admin'),

]