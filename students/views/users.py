from django.views.generic.base import TemplateView

from django.contrib.auth.models import User

from students.util import paginate


class UserView(TemplateView):
    """docstring for UserView
    This view takes User's id of url request and return User
    """
    template_name = 'registration/user.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        id = User.objects.get(pk=kwargs['pk'])
        context['username'] = id.username
        context['get_full_name'] = id.get_full_name
        context['email'] = id.email
        context['date_joined'] = id.date_joined.strftime('%d.%m.%Y')
        return self.render_to_response(context)


class UserList(TemplateView):
    """docstring for UserList"""
    template_name = 'students/users.html'

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(UserList, self).get_context_data(**kwargs)

        users = User.objects.all()

        # apply pagination, 10 users per page
        context = paginate(users, 10, self.request, context, var_name='users')

        return context
