from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic.edit import FormView

from students.forms.contact_admin import ContactForm

from studentsdb2.settings import ADMIN_EMAIL

import logging

from django.utils.translation import ugettext_lazy as _


class ContactView(PermissionRequiredMixin, FormView):
    template_name = 'contact_admin/form.html'
    form_class = ContactForm
    permission_required = 'auth.add_user'

    def get_success_url(self):
        return reverse('contact_admin')
    
    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']

        send_mail(subject, message, from_email, [ADMIN_EMAIL])
        messages.success(self.request, _('Message sended successfuly!'))
        return super(ContactView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, _('There was an unexpected error while sending the letter. Try using this form later.'))
        logger = logging.getLogger(__name__)
        logger.exception(messages)
        return super(ContactView, self).form_invalid(form)
