from django import forms
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from students.models import Exam, ExamResults

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions, AppendedText

from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', _('Send')))

    from_email = forms.EmailField(label=_('Your email'))

    subject = forms.CharField(label=_('Title message'), max_length=128)

    message = forms.CharField(label=_('Text message'), max_length=2560, widget=forms.Textarea)
