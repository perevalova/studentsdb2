# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django import forms
from django.core import serializers
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.forms import ModelForm


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions

from students.models import Student, Group
from .validation import valid_image_mimetype, valid_image_size

def students_list(request):
    students = Student.objects.all()

    #try to order students list
    order_by = request.GET.get('order_by', '')
    reverse = request.GET.get('reverse', '')
    if order_by in ('last_name', 'first_name', 'ticket', 'id'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    #paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})

class StudentAddForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'student_group', 'ticket', 'notes']

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(StudentAddForm, self).__init__(*args, **kwargs)
        
        #this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('students_add')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        #add buttons
        self.helper.layout[7] = FormActions(
            Submit('add_button', u'Додати', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
        )

class StudentAddView(CreateView):
    model = Student
    template_name = 'students/students_add.html'
    form_class = StudentAddForm

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, 'Додавання студента скасовано!')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request, 'Студента успішно додано!')
            return super(StudentAddView, self).post(request, *args, **kwargs)

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'student_group', 'ticket', 'notes']

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        
        #this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('students_edit', kwargs={'pk': kwargs['instance'].id})

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        #add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
        )

    def clean_student_group(self):
        """Check if student is leader in any group.
        If yes, then ensure it`s the same as selected group."""

        group = Group.objects.filter(leader=self.instance)
        if self.cleaned_data['student_group'] != group[0]:
                raise forms.ValidationError(u'Студент є старостою іншої групи.', code='invalid')
        
        return self.cleaned_data['student_group']


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        messages.success(request, 'Студента успішно збережено!')
        return HttpResponseRedirect(reverse('home'))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, 'Редагування студента відмінено!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'

    def get_success_url(self):
        messages.success(request, 'Студента успішно видалено!')
        return HttpResponseRedirect(reverse('home'))

# def students_visiting(request, sid):
    # return HttpResponse('<h1>Students Visiting %s</h1>' % sid)
