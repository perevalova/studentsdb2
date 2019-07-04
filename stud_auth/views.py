from django.views.generic.base import TemplateView

from django.contrib.auth.models import User
from .models import StProfile


class UserView(TemplateView):
    """docstring for UserView
    This view takes User's id of url request and return User
    """
    template_name = 'registration/user.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        id = User.objects.get(pk=kwargs['pk'])
        phone = StProfile.objects.get(pk=kwargs['pk'])
        context['username'] = id.username
        context['get_full_name'] = id.get_full_name
        context['email'] = id.email
        context['date_joined'] = id.date_joined.strftime('%d.%m.%Y')
        try:
            context['mobile_phone'] = phone.mobile_phone
        except Exception:
            context['mobile_phone'] = ''

        return self.render_to_response(context)