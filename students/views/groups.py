# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView

from students.models import Group

def groups_list(request):
    groups = Group.objects.all()

    #try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('leader', 'title'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    #paginate groups
    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If is out of range (e.g. 9999), deliver last page of results.
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/group_confirm_delete.html'

    def get_success_url(self):
        messages.success(request, 'Групу успішно видалено!')
        return HttpResponseRedirect(reverse('home'))
