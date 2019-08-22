# from modeltranslation.translator import translator, TranslationOptions
# from students.models import Student, Group, Exam, MonthJournal
#
# class StudentTranslationOptions(TranslationOptions):
#     fields = ('first_name', 'last_name', 'middle_name', 'notes',)
#
# class GroupTranslationOptions(TranslationOptions):
#     fields = ('title', 'leader', 'notes',)
#
# class ExamTranslationOptions(TranslationOptions):
#     fields = ('subject', 'teacher_first_name', 'teacher_last_name', 'teacher_middle_name',)
#
# class MonthJournalTranslationOptions(TranslationOptions):
#     fields = ('student',)
#
# translator.register(Student, StudentTranslationOptions)
# translator.register(Group, GroupTranslationOptions)
# translator.register(Exam, ExamTranslationOptions)
# translator.register(MonthJournal, MonthJournalTranslationOptions)