from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
# from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

from api.views import StudentViewSet, GroupViewSet, JournalViewSet, ExamViewSet, \
    ContactView


app_name = 'api'

API_TITLE = 'Students API'
API_DESCRIPTION = 'A Web API for creating and editing students, groups and exams.'
schema_view = get_swagger_view(title=API_TITLE)

router = DefaultRouter()
router.register('students', StudentViewSet, base_name='students')
router.register('groups', GroupViewSet, base_name='groups')
router.register('journal', JournalViewSet, base_name='journal')
router.register('exams', ExamViewSet, base_name='exams')

urlpatterns = [
    path('contact-admin/', ContactView.as_view(), name='contact_admin'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # path('schema/', schema_view),
    path('swagger-docs/', schema_view),
]

urlpatterns += router.urls
