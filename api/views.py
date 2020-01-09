from rest_framework import generics, viewsets
from students.models import Student, Group, Exam, MonthJournal
from .serializers import StudentSerializer, GroupSerializer, ExamSerializer, \
    MonthJournalSerializer, ContactAdminSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class JournalViewSet(viewsets.ModelViewSet):
    queryset = MonthJournal.objects.all()
    serializer_class = MonthJournalSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ContactView(generics.CreateAPIView):
    serializer_class = ContactAdminSerializer
