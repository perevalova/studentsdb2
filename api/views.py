from rest_framework import generics, viewsets, filters
from students.models import Student, Group, Exam, MonthJournal
from .serializers import StudentSerializer, GroupSerializer, ExamSerializer, \
    MonthJournalSerializer, ContactAdminSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['last_name', 'student_group__title']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class JournalViewSet(viewsets.ModelViewSet):
    queryset = MonthJournal.objects.all()
    serializer_class = MonthJournalSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['student__last_name']
    ordering_fields = ['date', 'student__last_name']
    ordering = ['student__last_name']


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['subject', 'exam_group__title']
    ordering_fields = ['date', 'subject']


class ContactView(generics.CreateAPIView):
    serializer_class = ContactAdminSerializer
