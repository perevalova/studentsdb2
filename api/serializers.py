from django.core.mail import send_mail
from rest_framework import serializers
from students.models import Student, Group, Exam, MonthJournal
from studentsdb2.settings import ADMIN_EMAIL


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        fields = ('url', 'id', 'title', 'leader', 'notes',)
        model = Group
        extra_kwargs = {
            'url': {'view_name': 'api:groups-detail'},
            'leader': {'view_name': 'api:groups-detail'},
        }


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='api:students-detail',)

    class Meta:
        fields = ('url', 'id', 'first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'student_group', 'ticket', 'notes',)
        model = Student
        extra_kwargs = {
            'url': {'view_name': 'api:students-detail'},
            'student_group': {'view_name': 'api:groups-detail'},
        }


class MonthJournalSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = MonthJournal


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('url', 'id', 'subject', 'teacher_first_name', 'teacher_last_name',
                  'teacher_middle_name', 'date', 'exam_group',)
        model = Exam
        extra_kwargs = {
            'url': {'view_name': 'api:exams-detail'},
            'exam_group': {'view_name': 'api:groups-detail'},
        }


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
