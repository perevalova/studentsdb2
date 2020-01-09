from rest_framework import serializers
from students.models import Student, Group, Exam


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'birthday', 'photo',
                  'student_group', 'ticket', 'notes',)
        model = Student


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'leader', 'notes',)
        model = Group
        depth = 1


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'subject', 'teacher_first_name', 'teacher_last_name',
                  'teacher_middle_name', 'date', 'exam_group',)
        model = Exam
        depth = 1


# class ExamResultsSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'subject_exam', 'student', 'grade',)
#         model = ExamResults
