# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView

from students.models import Exam

def exams_list(request):
    exams = Exam.objects.all()

    #try to order exams list
    order_by = request.GET.get('order_by', '')
    reverse = request.GET.get('reverse', '')
    if order_by in ('subject', 'exam_group', 'data', 'teacher_first_name', 'teacher_last_name'):
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

def exams_add(request):
    return HttpResponse('<h1>Exam Add Form</h1>')

def exams_edit(request, eid):
    return HttpResponse('<h1>Edit Exam %s</h1>' % eid)

def exams_delete(request, eid):
    return HttpResponse('<h1>Delete Exam %s</h1>' % eid)
