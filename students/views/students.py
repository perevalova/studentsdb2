# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView

from students.models import Student, Group

def students_list(request):
    students = Student.objects.all()

#class StudentList(TemplateView):
    #template_name = 'students/students_list.html'

    #def get_context_data(self, **kwargs):
        #context = super(StudentList, self).get_context_data(**kwargs)

        #students = Student.objects.all()

    # Order students list
        #order_by = self.request.GET.get('order_by', '') # Витягуємо параметр order_by з GET словника
        #reverse = self.request.GET.get('reverse', '') # Витягуємо параметр reverse з GET словника

        #if order_by in ('last_name', 'first_name', 'ticket', 'id'):
        #   students = students.order_by(order_by)
        #   if reverse == '1':
        #       students = students.reverse()

        #context = paginate(students, 3, self.request, context, var_name='students')

        #return context

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

def students_add(request):
    # Was form posted?
    if request.method == "POST":
        # Was form add button clicked?
        if request.POST.get('add_button') is not None:

            # TODO: validate input from user
            errors = {}

            if not errors:
                # create student object
                student = Student(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    middle_name=request.POST['middle_name'],
                    birthday=request.POST['birthday'],
                    ticket=request.POST['ticket'],
                    student_group=Group.objects.get(pk=request.POST['student_group']),
                    photo=request.FILES['photo'],
                )

                # save it to database
                student.save()

                # redirect user to students list
                return HttpResponseRedirect(reverse('home'))

            else:
                #render form with errors and previous user input
                return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title'), 'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})
        
    return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# def students_visiting(request, sid):
    # return HttpResponse('<h1>Students Visiting %s</h1>' % sid)
