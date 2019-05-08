# -*- coding: utf-8 -*-

from django.db import models


class Student(models.Model):
    """Student Model"""

    class Meta(object):
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенти"
        ordering = ['last_name']

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ім'я")

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище")

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"По батькові",
        default='')

    birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата народження",
        null=True)

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True)

    student_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Білет")

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    """id = models.CharField(
        max_length=256,
        blank=False,
        primary_key=True,
        verbose_name="№")"""

    def __str__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Group(models.Model):
    """Group Model"""

    class Meta(object):
        verbose_name = u"Група"
        verbose_name_plural = u"Групи"
        ordering = ['title']

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")

    leader = models.OneToOneField('Student',
        verbose_name=u"Староста",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    def __str__(self):
        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return u"%s" % self.title


class MonthJournal(models.Model):
    """Student Monthly Journal"""

    class Meta:
        verbose_name = u"Місячний Журнал"
        verbose_name_plural = u"Місячні Журнали"

    student = models.ForeignKey('Student',
        unique_for_month='date',
        blank=False,
        verbose_name=u"Студент")

    date = models.DateField(
        verbose_name=u'Дата',
        blank=False)

    def __str__(self):
        return u"%s: %d, %d" % (self.student.last_name, self.date.month, self.date.year)


local_vars = locals()
for num in range(1, 32):
    local_vars.update({'present_day'+str(num): models.BooleanField(default=False)})


class Exam(models.Model):
    """Exam Model"""

    class Meta(object):
        verbose_name = u"Іспит"
        verbose_name_plural = u"Іспити"
        ordering = ['subject']

    subject = models.CharField(
        max_length=256,
        verbose_name=u"Назва предмету",
        blank=False)

    teacher_first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ім'я")

    teacher_last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище")

    teacher_middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"По батькові",
        default='')

    date = models.DateField(
        blank=False,
        verbose_name=u"Дата іспиту",
        null=True)

    exam_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    def __str__(self):
        return u"%s" % self.subject


class ExamResults(models.Model):
    """Exam Results Model"""

    class Meta(object):
        verbose_name = u"Результат Іспиту"
        verbose_name_plural = u"Результати Іспитів"

    subject_exam = models.ForeignKey('Exam',
        verbose_name=u"Предмет",
        max_length=256,
        blank=False)

    student = models.ForeignKey('Student',
        verbose_name=u"Студент",
        blank=True,
        null=True)

    grade = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Оцінка",
        null=True)

    def __str__(self):
        return u"%s (%s)" % (self.student, self.student.student_group)
