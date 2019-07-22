from django.views.generic import DetailView
from django.views.generic.base import TemplateView

from django.contrib.auth.models import User

from students.util import paginate


class UserView(DetailView):
    """docstring for UserView
    This view takes User's id of url request and return User
    """
    template_name = 'registration/user.html'
    model = User


class UserList(TemplateView):
    """docstring for UserList"""
    template_name = 'registration/users.html'

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(UserList, self).get_context_data(**kwargs)

        users = User.objects.order_by('username')
        # users = StProfile.objects.order_by('user__username')

        # apply pagination, 10 users per page
        context = paginate(users, 10, self.request, context, var_name='users')

        return context
