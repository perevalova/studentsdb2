from django.conf.urls import url
from .views import StudentList, StudentDetail, GroupList, GroupDetail, ExamList, \
    ExamDetail


urlpatterns = [
    url(r'^students/$', StudentList.as_view(), name='students'),
    url(r'^students/(?P<pk>\d+)/$', StudentDetail.as_view(), name='students_detail'),

    # Groups urls
    url(r'^groups/$', GroupList.as_view(), name='groups'),
    url(r'^groups/(?P<pk>\d+)/$', GroupDetail.as_view(), name='groups_detail'),

    # Visiting urls
    # url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    # Exams urls
    url(r'^exams/$', ExamList.as_view(), name='exams'),
    url(r'^exams/(?P<pk>\d+)/$', ExamDetail.as_view(), name='exams_detail'),
]