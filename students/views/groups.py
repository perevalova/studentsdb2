from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.views.generic import UpdateView
from students.models import Group, Student
from students.forms.groups import GroupAddForm, GroupUpdateForm

from students.util import paginate, get_current_group

from django.utils.translation import ugettext as _


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

        search_group = self.request.GET.get('search', '')
        if search_group:
            groups = Group.objects.filter(title__icontains=search_group)
        #TODO: show message if request doesn't match any query

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


class GroupAddView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'students/groups_add.html'
    form_class = GroupAddForm

    def get_success_url(self):
        return reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, _('Group adding has been canceled!'))
            return HttpResponseRedirect(reverse('groups'))
        else:
            messages.success(request, _('Group added successfully!'))
            return super(GroupAddView, self).post(request, *args, **kwargs)


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupUpdateForm

    def get_success_url(self):
        return reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, _('Group adding has been canceled!'))
            return HttpResponseRedirect(reverse('groups'))
        else:
            messages.success(request, _('Group saved successfully!'))
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'students/group_confirm_delete.html'

    def get_success_url(self):
        return reverse('groups')

    def post(self, request, *args, **kwargs):
        group = Group.objects.filter(student__student_group=kwargs['pk'])
        if group:
            messages.warning(request, _('Deleting a group that has students is forbidden! Remove all students first.'))
            return HttpResponseRedirect(reverse('groups'))
        else:
            messages.success(request, _('Group deleted successfully!'))
            return super(GroupDeleteView, self).post(request, *args, **kwargs)
