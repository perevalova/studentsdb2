# -*- coding: utf-8 -*-

from django.shortcuts import render
from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.views.generic import UpdateView
from django.forms import ModelForm, ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions, AppendedText

from students.models import Group, Student

from students.util import paginate, get_current_group


class GroupList(TemplateView):
    """docstring for GroupList"""
    template_name = 'students/groups_list.html'

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(GroupList, self).get_context_data(**kwargs)

        current_group = get_current_group(self.request)

        if current_group:
            groups = Group.objects.filter(pk=current_group.pk)
        else:
            # otherwise show all students
            groups = Group.objects.all()

        # try to order groups list
        order_by = self.request.GET.get('order_by', '')
        reverse = self.request.GET.get('reverse', '')
        if order_by in ('leader', 'title'):
            groups = groups.order_by(order_by)
            if self.request.GET.get('reverse', '') == '1':
                groups = groups.reverse()

        # apply pagination, 10 students per page
        context = paginate(groups, 10, self.request, context, var_name='groups')

        return context


class GroupAddForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'leader', 'notes']

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(GroupAddForm, self).__init__(*args, **kwargs)
        
        # this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('groups_add')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout = Layout(
            'title', 'leader', 'notes',
            FormActions(
                Submit('add_button', u'Додати', css_class="btn btn-primary"),
                Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
            )
        )


class GroupAddView(CreateView):
    model = Group
    template_name = 'students/groups_add.html'
    form_class = GroupAddForm

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, 'Додавання групи скасовано!')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request, 'Групу успішно додано!')
            return super(GroupAddView, self).post(request, *args, **kwargs)


class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'leader', 'notes']

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(GroupUpdateForm, self).__init__(*args, **kwargs)
        
        # this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('groups_edit', kwargs={'pk': kwargs['instance'].id})

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout = Layout(
            'title', 'leader', 'notes',
            FormActions(
                Submit('add_button', u'Додати', css_class="btn btn-primary"),
                Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
            )
        )

    def clean_leader(self):
        """Check if student is leader in any group.
        If yes, then ensure it's the same as selected group."""
        # get group where current student is a leader
        leaders = Student.objects.filter(student_group=self.instance)
        if len(leaders) > 0 and self.cleaned_data['leader'] != leaders[0]:
            raise ValidationError(u'Студент не належить до поточної групи.', code='invalid')

        return self.cleaned_data['leader']


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupUpdateForm

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, 'Редагування групи відмінено!')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request, 'Групу успішно збережено!')
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/group_confirm_delete.html'

    def get_success_url(self):
        return HttpResponseRedirect(reverse('home'))

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Групу успішно видалено!')
        return super(GroupDeleteView, self).post(request, *args, **kwargs)
