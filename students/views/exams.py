# -*- coding: utf-8 -*-

from django import forms
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.views.generic import UpdateView
from django.forms import ModelForm, ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions

from students.models import Exam, ExamResults

def exams_list(request):
    exams = Exam.objects.all()

    #try to order exams list
    order_by = request.GET.get('order_by', '')
    reverse = request.GET.get('reverse', '')
    if order_by in ('subject', 'exam_group', 'date', 'teacher_first_name', 'teacher_last_name'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    #paginate exams
    paginator = Paginator(exams, 3)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exams = paginator.page(1)
    except EmptyPage:
        # If is out of range (e.g. 9999), deliver last page of results.
        exams = paginator.page(paginator.num_pages)

    return render(request, 'students/exams_list.html', {'exams': exams})

class ExamAddForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ExamAddForm, self).__init__(*args, **kwargs)
        
        #this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('exams_add')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        #add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Додати', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
        )

class ExamAddView(CreateView):
    model = Exam
    template_name = 'students/exams_add.html'
    form_class = ExamAddForm

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, 'Додавання екзамену скасовано!')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request, 'Екзамен успішно додано!')
            return super(ExamAddView, self).post(request, *args, **kwargs)


class ExamUpdateForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ExamUpdateForm, self).__init__(*args, **kwargs)
        
        #this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('exams_edit', kwargs={'pk': kwargs['instance'].id})

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

class ExamUpdateView(UpdateView):
    model = Exam
    template_name = 'students/exams_edit.html'
    form_class = ExamUpdateForm

    def get_success_url(self):
        messages.success(request, 'Екзамен успішно збережено!')
        return HttpResponseRedirect(reverse('home'))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, 'Редагування екзамену відмінено!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(ExamUpdateView, self).post(request, *args, **kwargs)

class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'students/exam_confirm_delete.html'

    def get_success_url(self):
        messages.success(request, 'Екзамен успішно видалено!')
        return HttpResponseRedirect(reverse('home'))

def exams_results(request, arg1, arg2):
    results = ExamResults.objects.filter(student_group__title='%s' % arg1).filter(subject_exam__subject_exam='%s' % arg2)
    results.order_by('student')

    return render(request, 'students/exams_results.html', {'results': results})
