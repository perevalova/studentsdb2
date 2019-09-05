from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.views.generic import UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView

from students.forms.students import StudentAddForm, StudentUpdateForm
from students.models import Student
from students.util import paginate, get_current_group


class StudentList(TemplateView):
    """docstring for StudentList"""
    template_name = 'students/students_list.html'

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(StudentList, self).get_context_data(**kwargs)

        current_group = get_current_group(self.request)
        if current_group:
            students = Student.objects.filter(student_group=current_group)
        else:
            students = Student.objects.all()

        search_student = self.request.GET.get('search', '')
        if search_student:
            # students = Student.objects.filter(first_name__icontains=search_student, last_name__icontains=search_student)
            students = Student.objects.filter(Q(first_name__icontains=search_student) | Q(last_name__icontains=search_student))
        #TODO: show message if request doesn't match any query

        # try to order students list
        order_by = self.request.GET.get('order_by', '')
        reverse = self.request.GET.get('reverse', '')
        if order_by in ('last_name', 'first_name', 'ticket', 'id'):
            students = students.order_by(order_by)
            if self.request.GET.get('reverse', '') == '1':
                students = students.reverse()

        # apply pagination, 10 students per page
        context = paginate(students, 10, self.request, context, var_name='students')

        return context


class StudentAddView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'students/students_add.html'
    form_class = StudentAddForm

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, _('Student adding has been canceled!'))
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request, _('Student added successfully!'))
            return super(StudentAddView, self).post(request, *args, **kwargs)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, _('Student editing has been canceled!'))
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request, _('Student updated successfully!'))
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        messages.success(request, _('Student deleted successfully!'))
        return super(StudentDeleteView, self).post(request, *args, **kwargs)
