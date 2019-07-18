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
        users_obj = User.objects.get(pk=kwargs['pk'])
        context['username'] = users_obj.username
        context['full_name'] = users_obj.get_full_name
        context['email'] = users_obj.email
        context['date_joined'] = users_obj.date_joined.strftime('%d.%m.%Y')
        try:
            context['photo'] = users_obj.stprofile.photo
            context['mobile_phone'] = users_obj.stprofile.mobile_phone
            context['passport'] = users_obj.stprofile.passport
        except Exception:
            context['photo'] = ''
            context['passport'] = ''
            context['mobile_phone'] = ''

        return self.render_to_response(context)


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
