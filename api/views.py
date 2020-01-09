from rest_framework import generics
from students.models import Student, Group, Exam, MonthJournal
from .serializers import StudentSerializer, GroupSerializer, ExamSerializer, \
    MonthJournalSerializer, ContactAdminSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class JournalList(generics.ListCreateAPIView):
    queryset = MonthJournal.objects.all()
    serializer_class = MonthJournalSerializer


class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonthJournal.objects.all()
    serializer_class = MonthJournalSerializer


class ExamList(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ContactView(generics.CreateAPIView):
    serializer_class = ContactAdminSerializer
