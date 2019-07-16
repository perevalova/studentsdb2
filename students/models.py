from django.db import models
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):
    """Student Model"""

    first_name = models.CharField(max_length=256, blank=False, verbose_name=_("First name"))
    last_name = models.CharField(max_length=256, blank=False, verbose_name=_("Last name"))
    middle_name = models.CharField(max_length=256, blank=True, verbose_name=_("Middle name"), default='')
    birthday = models.DateField(blank=False, verbose_name=_("Birth date"), null=True)
    photo = models.ImageField(blank=True, verbose_name=_("Photo"), null=True)
    student_group = models.ForeignKey('Group', verbose_name=_("Group"), blank=False, null=True, on_delete=models.PROTECT)
    ticket = models.PositiveIntegerField(unique=True, blank=False, verbose_name=_("Ticket"))
    notes = models.TextField(blank=True, verbose_name=_("Additional notes"))

    class Meta(object):
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
        ordering = ['last_name']

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Group(models.Model):
    """Group Model"""

    title = models.CharField(max_length=256, blank=False, verbose_name=_("Title"))
    leader = models.OneToOneField(Student, verbose_name=_("Leader"), blank=True, null=True, on_delete=models.SET_NULL)
    notes = models.TextField(blank=True, verbose_name=_("Additional notes"))

    class Meta(object):
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")
        ordering = ['title']

    def __str__(self):
        if self.leader:
            return "%s (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return "%s" % self.title


class MonthJournal(models.Model):
    """Student Monthly Journal"""

    student = models.ForeignKey(Student, unique_for_month='date', blank=False, verbose_name=_("Student"))
    date = models.DateField(verbose_name=_('Date'), blank=False)

    class Meta:
        verbose_name = _("Month Journal")
        verbose_name_plural = _("Month Journals")

    def __str__(self):
        return "%s: %d, %d" % (self.student.last_name, self.date.month, self.date.year)


for num in range(1, 32):
    MonthJournal.add_to_class('present_day'+str(num), models.BooleanField(default=False))


class Exam(models.Model):
    """Exam Model"""

    subject = models.CharField(max_length=256, verbose_name=_("Title subject"), blank=False)
    teacher_first_name = models.CharField(max_length=256, blank=False, verbose_name=_("First name"))
    teacher_last_name = models.CharField(max_length=256, blank=False, verbose_name=_("Last name"))
    teacher_middle_name = models.CharField(max_length=256, blank=True, verbose_name=_("Middle name"), default='')
    date = models.DateField(blank=False, verbose_name=_("Date exam"), null=True)
    exam_group = models.ForeignKey(Group, verbose_name=_("Group"), blank=False, null=True, on_delete=models.PROTECT)

    class Meta(object):
        verbose_name = _("Exam")
        verbose_name_plural = _("Exams")
        ordering = ['subject']

    def __str__(self):
        return u"%s" % self.subject


class ExamResults(models.Model):
    """Exam Results Model"""

    subject_exam = models.ForeignKey(Exam, verbose_name=_("Subject"), max_length=256, blank=False)
    student = models.ForeignKey(Student, verbose_name=_("Student"), blank=True, null=True)
    grade = models.CharField(max_length=256,  blank=False, verbose_name=_("Grade"), null=True)

    class Meta(object):
        verbose_name = _("The result of the exam")
        verbose_name_plural = _("The results of the exams")

    def __str__(self):
        return "%s (%s)" % (self.student, self.student.student_group)
