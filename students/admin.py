import mimetypes
import os

from django.contrib import admin, messages
from django.urls import reverse
from django.forms import ModelForm, ValidationError
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from inline_actions.admin import InlineActionsMixin
from inline_actions.admin import InlineActionsModelAdminMixin

from .models import Student, Group, Exam, ExamResults, MonthJournal, Document, \
    Type


class DocumentInline(InlineActionsMixin, admin.TabularInline):
    model = Document
    template = "admin/students/student/tabular.html"
    fields = ['name', 'type', 'file']
    inline_actions = ['view', 'download', 'print', 'delete']
    extra = 1

    def get_view_css(self, obj):
        return 'input-view'

    def get_download_css(self, obj):
        return 'input-download'

    def get_print_css(self, obj):
        return 'input-print'

    def get_delete_css(self, obj):
        return 'input-delete'

    def view(self, request, obj, parent_obj=None):
        """View selected file"""
        if obj.file:
            return redirect(obj.file.url)
        else:
            return "No attachment"
    view.short_description = "View"

    def print(self, request, obj, parent_obj=None):
        """Print selected file"""
    print.short_description = "Print"

    # def print(self, request, obj, parent_obj=None):
    #     """Download selected file"""
    #     file_path = '%s' % obj.file.file
    #     filename = os.path.basename(file_path)
    #     if os.path.exists(file_path):
    #         if platform.system() == "Windows":
    #             os.startfile(file_path, "print")
    #         elif platform.system() == "Darwin":
    #             subprocess.call(["open", file_path])
    #         else:
    #             if filename.endswith((".doc", ".docx")):
    #                 subprocess.call(["xdg-open", file_path])
    #             else:
    #                 subprocess.call(["lpr", file_path])
    # print.short_description = "Print"

    def download(self, request, obj, parent_obj=None):
        """Download selected file"""
        file_path = '%s' % obj.file.file
        filename = os.path.basename(file_path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(),
                                        content_type=mimetypes.guess_type(filename)[0])
                response['Content-Disposition'] = 'attachment; filename=%s' % filename
                return response
        raise Http404
    download.short_description = 'Download'

    def delete(self, request, obj, parent_obj=None):
        """Redirect to delete confirmation of selected inline instance"""
        if request.user.is_superuser:
            url = reverse(
                'admin:{}_{}_delete'.format(
                    obj._meta.app_label,
                    obj._meta.model_name,
                ),
                args=(obj.pk,)
            )
            return redirect(url)
        else:
            messages.error(request, "You don't have permission to delete it.")
    delete.short_description = _("Delete")

    # def delete(self, request, obj, parent_obj=None):
    #     """Remove selected inline instance if permission is sufficient"""
    #     if self.has_delete_permission(request):
    #         obj.delete()
    #         messages.info(request, "`{}` deleted.".format(obj))
    #     else:
            # messages.error(request, "You don't have permission to delete it.")

    class Media:
        js = ("js/print.js",)


class StudentFormAdmin(ModelForm):

    def clean_student_group(self):
        """Check if student is leader in any group.
        If yes, then ensure it's the same as selected group."""
        # get group where current student is a leader
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(_('Student is a leader of a different group.'), code='invalid')

        return self.cleaned_data['student_group']


class StudentAdmin(InlineActionsModelAdminMixin, admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket']
    form = StudentFormAdmin
    inlines = (DocumentInline,)

    @staticmethod
    def view_on_site(obj):
        return reverse('students_edit', kwargs={'pk': obj.id})


class GroupFormAdmin(ModelForm):

    def clean_leader(self):
        """Check if student is leader in any group.
        If yes, then ensure it's the same as selected group."""
        # get group where current student is a leader
        leaders = Student.objects.filter(student_group=self.instance)
        if len(leaders) > 0 and self.cleaned_data['leader'] != leaders[0]:
            raise ValidationError(_('Student does not belong to the current group.'), code='invalid')

        return self.cleaned_data['leader']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader']
    list_display_links = ['title', 'leader']
    ordering = ['title']
    list_per_page = 10
    search_fields = ['title', 'leader', 'notes']
    form = GroupFormAdmin

    @staticmethod
    def view_on_site(obj):
        return reverse('groups_edit', kwargs={'pk': obj.id})


class ExamAdmin(admin.ModelAdmin):
    list_display = ['subject', 'date', 'teacher_first_name', 'teacher_last_name', 'exam_group']
    list_display_links = ['subject']
    list_editable = ['exam_group']
    ordering = ['date']
    list_per_page = 10
    search_fields = ['subject', 'date', 'teacher_first_name', 'teacher_last_name', 'exam_group']

    @staticmethod
    def view_on_site(obj):
        return reverse('exams_edit', kwargs={'pk': obj.id})


class ExamResultsAdmin(admin.ModelAdmin):
    list_display = ['subject_exam', 'student', 'grade']
    list_display_links = ['subject_exam']
    ordering = ['student']
    list_per_page = 10
    search_fields = ['subject_exam', 'student', 'grade']

    @staticmethod
    def view_on_site(obj):
        return reverse('exams_edit', kwargs={'pk': obj.id})


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamResults, ExamResultsAdmin)
admin.site.register(MonthJournal)
admin.site.register(Type)
admin.site.register(Document)
