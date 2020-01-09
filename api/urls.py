from django.conf.urls import url
from django.contrib.auth.decorators import permission_required

from rest_framework.routers import SimpleRouter

from api.views import StudentViewSet, GroupViewSet, JournalViewSet, ExamViewSet, \
    ContactView

router = SimpleRouter()
router.register('students', StudentViewSet, base_name='students')
router.register('groups', GroupViewSet, base_name='groups')
router.register('journal', JournalViewSet, base_name='journal')
router.register('exams', ExamViewSet, base_name='exams')

urlpatterns = [
    url(r'^contact-admin/$', permission_required('auth.add_user')(ContactView.as_view()),
        name='contact_admin'),
]

urlpatterns += router.urls
