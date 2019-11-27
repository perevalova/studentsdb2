from rest_framework import serializers
from students.models import Student, Group, Exam


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'middle_name', 'birthday', 'photo',
                  'student_group', 'ticket', 'notes',)
        model = Student


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'leader', 'notes',)
        model = Group


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('subject', 'teacher_first_name', 'teacher_last_name',
                  'teacher_middle_name', 'date', 'exam_group',)
        model = Exam


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('subject', 'teacher_first_name', 'teacher_last_name',
                  'teacher_middle_name', 'date', 'exam_group',)
        model = Exam
