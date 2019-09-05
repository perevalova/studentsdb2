from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse, request
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.views.generic import UpdateView

from students.models import Exam, ExamResults
from students.forms.exams import ExamAddForm, ExamUpdateForm

from students.util import paginate, get_current_group

from django.utils.translation import ugettext as _


class ExamList(TemplateView):
    """docstring for ExamList"""
    template_name = 'students/exams_list.html'

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(ExamList, self).get_context_data(**kwargs)

        current_group = get_current_group(self.request)

        if current_group:
            exams = Exam.objects.filter(exam_group=current_group)
        else:
            # otherwise show all students
            exams = Exam.objects.all()


        search_exam = self.request.GET.get('search', '')
        if search_exam:
            # students = Student.objects.filter(first_name__icontains=search_student, last_name__icontains=search_student)
            exams = Exam.objects.filter(subject__icontains=search_exam)
        #TODO: show message if request doesn't match any query

        # try to order exams list
        order_by = self.request.GET.get('order_by', '')
        reverse = self.request.GET.get('reverse', '')
        if order_by in ('subject', 'exam_group', 'date', 'teacher_first_name', 'teacher_last_name'):
            exams = exams.order_by(order_by)
            if self.request.GET.get('reverse', '') == '1':
                exams = exams.reverse()

        # apply pagination, 10 students per page
        context = paginate(exams, 10, self.request, context, var_name='exams')

        return context


class ExamAddView(LoginRequiredMixin, CreateView):
    model = Exam
    template_name = 'students/exams_add.html'
    form_class = ExamAddForm

    def get_success_url(self):
        return reverse('exams')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, _('Exam adding has been canceled!'))
            return HttpResponseRedirect(reverse('exams'))
        else:
            messages.success(request, _('Exam added successfully!'))
            return super(ExamAddView, self).post(request, *args, **kwargs)


class ExamUpdateView(LoginRequiredMixin, UpdateView):
    model = Exam
    template_name = 'students/exams_edit.html'
    form_class = ExamUpdateForm

    def get_success_url(self):
        return reverse('exams')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, _('Exam editing has been canceled!'))
            return HttpResponseRedirect(reverse('exams'))
        else:
            messages.success(request, _('Exam saved successfully!'))
            return super(ExamUpdateView, self).post(request, *args, **kwargs)


class ExamDeleteView(LoginRequiredMixin, DeleteView):
    model = Exam
    template_name = 'students/exam_confirm_delete.html'

    def get_success_url(self):
        return reverse('exams')

    def post(self, request, *args, **kwargs):
        messages.success(request, _('Exam deleted successfully!'))
        return super(ExamDeleteView, self).post(request, *args, **kwargs)
