from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, request
# from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, UpdateView
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext as _

from django.contrib.auth.models import User

from stud_auth.forms.form import StProfileEditForm, UserEditForm
from stud_auth.models import StProfile
from students.util import paginate


class UserView(DetailView):
    template_name = 'registration/user.html'
    model = User


class UserEditView(UpdateView):
    template_name = 'registration/profile_edit.html'
    model = User
    form_class = UserEditForm

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.id)

    def get_success_url(self):
        return reverse('profile_edit')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, _('User editing has been canceled!'))
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.success(request, _('User profile was editing successfully!'))
            return super(UserEditView, self).post(request, *args, **kwargs)

#
# class UserEditView(UpdateView):
#     template_name = 'registration/profile_edit.html'
#     model = User
#     form_class = UserEditForm
#     second_form_class = StProfileEditForm
#
#     def get_object(self):
#         return get_object_or_404(User, pk=self.request.user.id)
#
#     def get_success_url(self):
#         return reverse('profile')
#
#     def get_context_data(self, **kwargs):
#         context = super(UserEditView, self).get_context_data(**kwargs)
#         context['second_form'] = self.second_form_class(self.request.GET or None,
#                                                       instance=self.request.user.stprofile)
#
#         return context
#
#     def post(self, request, *args, **kwargs):
#         self.first_form = UserEditForm(request.POST, instance=request.user, prefix='first_form')
#         self.second_form = StProfileEditForm(request.POST, instance=request.user.stprofile, prefix='second_form')
#         if self.first_form.is_valid():
#             self.first_form.save()
#         if self.second_form.is_valid():
#             self.second_form.save()
#
#         if request.POST.get('cancel_button'):
#             messages.warning(request, _('User editing has been canceled!'))
#             return HttpResponseRedirect(reverse('profile'))
#         else:
#             messages.success(request, _('User profile was editing successfully!'))
#             return super(UserEditView, self).post(request, *args, **kwargs)
#

class UserExtraEditView(UpdateView):
    template_name = 'registration/profile_extra_edit.html'
    model = StProfile
    form_class = StProfileEditForm

    def get_object(self, queryset=None):
        obj, created = StProfile.objects.get_or_create(user=self.request.user)
        return obj

    def get_success_url(self):
        return reverse('profile_extra_edit')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.warning(request, _('User editing has been canceled!'))
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.success(request, _('User profile was editing successfully!'))
            return super(UserExtraEditView, self).post(request, *args, **kwargs)


class UserList(TemplateView):
    template_name = 'registration/users.html'

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(UserList, self).get_context_data(**kwargs)

        users = User.objects.order_by('username')
        # users = StProfile.objects.order_by('user__username')

        # apply pagination, 10 users per page
        context = paginate(users, 10, self.request, context, var_name='users')

        return context
