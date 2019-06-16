import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Student, Group, Exam, MonthJournal


@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated student into log file"""
    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    if kwargs['created']:
        logger.info("Student added: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
    else:
        logger.info("Student updated: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
    print(sender)


@receiver(post_delete, sender=Student)
def log_student_delete_event(sender, **kwargs):
    """Writes information about deleted student into log file"""
    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    logger.info("Student deleted: %s %s (ID: %d)", student.first_name, student.last_name, student.id)
    print(sender)


@receiver(post_save, sender=Group)
def log_group_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated group into log file"""
    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    if kwargs['created']:
        logger.info("Group added: %s %s %s (ID: %d)", group.title, group.leader.first_name, group.leader.last_name, group.id)
    else:
        logger.info("Group updated: %s %s %s (ID: %d)", group.title, group.leader.first_name, group.leader.last_name, group.id)
    print(sender)


@receiver(post_delete, sender=Group)
def log_group_delete_event(sender, **kwargs):
    """Writes information about deleted group into log file"""
    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    logger.info("Group deleted: %s %s %s (ID: %d)", group.title, group.leader.first_name, group.leader.last_name, group.id)
    print(sender)


@receiver(post_save, sender=Exam)
def log_exam_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated exam into log file"""
    logger = logging.getLogger(__name__)

    exam = kwargs['instance']
    if kwargs['created']:
        logger.info("Exam added: %s %s (ID: %d)", exam.subject, exam.exam_group, exam.id)
    else:
        logger.info("Exam updated: %s %s (ID: %d)", exam.subject, exam.exam_group, exam.id)
    print(sender)


@receiver(post_delete, sender=Exam)
def log_exam_delete_event(sender, **kwargs):
    """Writes information about deleted student into log file"""
    logger = logging.getLogger(__name__)

    exam = kwargs['instance']
    logger.info("Exam deleted: %s %s (ID: %d)", exam.subject, exam.exam_group, exam.id)
    print(sender)


@receiver(post_save, sender=MonthJournal)
def log_journal_updated_added_event(sender, **kwargs):
    """Writes information about newly added or updated journal into log file"""
    logger = logging.getLogger(__name__)

    journal = kwargs['instance']
    if kwargs['created']:
        logger.info("Journal added: %s %s (ID: %d)", journal.student.last_name, journal.student.first_name, journal.id)
    else:
        logger.info("Journal updated: %s %s (ID: %d)", journal.student.last_name, journal.student.first_name, journal.id)
    print(sender)


@receiver(post_delete, sender=MonthJournal)
def log_journal_delete_event(sender, **kwargs):
    """Writes information about deleted journal into log file"""
    logger = logging.getLogger(__name__)

    journal = kwargs['instance']
    logger.info("Journal deleted: %s %s (ID: %d)", journal.student.last_name, journal.student.first_name, journal.id)
    print(sender)