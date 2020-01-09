from django.core.mail import send_mail
from rest_framework import serializers
from students.models import Student, Group, Exam, MonthJournal
from studentsdb2.settings import ADMIN_EMAIL


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'birthday', 'photo',
                  'student_group', 'ticket', 'notes',)
        model = Student
        depth = 1


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'leader', 'notes',)
        model = Group
        depth = 1


class MonthJournalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'student', 'date',)
        model = MonthJournal
        depth = 1


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'subject', 'teacher_first_name', 'teacher_last_name',
                  'teacher_middle_name', 'date', 'exam_group',)
        model = Exam
        depth = 1


class ContactAdminSerializer(serializers.Serializer):
    from_email = serializers.EmailField(label='Your email')
    subject = serializers.CharField(label='Title message', max_length=128)
    message = serializers.CharField(label='Text message', max_length=2560)

    def save(self):
        from_email = self.validated_data['from_email']
        subject = self.validated_data['subject']
        message = self.validated_data['message']
        send_mail(subject, message, from_email, [ADMIN_EMAIL])


# class ExamResultsSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'subject_exam', 'student', 'grade',)
#         model = ExamResults
