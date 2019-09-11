from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.bootstrap import FormActions

from django.utils.translation import ugettext as _

from stud_auth.models import StProfile


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(UserEditForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('profile_edit')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout = Layout(
            'username', 'first_name', 'last_name', 'email',
            FormActions(
                Submit('save_button', _('Save'), css_class="btn btn-primary"),
                Submit('cancel_button', _('Cancel'), css_class="btn btn-link"),
            )
        )


class StProfileEditForm(ModelForm):
    # def get_photo(self, obj):
    #     return obj.stprofile.get_photo()

    class Meta:
        model = StProfile
        fields = ['photo', 'mobile_phone', 'passport', 'city', 'street', 'house']

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(StProfileEditForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('profile_extra_edit')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout = Layout(
            # HTML('<img src="%s" width="50" height="50"/>' % StProfile.get_photo()),
             'photo', 'mobile_phone', 'passport', 'city', 'street', 'house',
            FormActions(
                Submit('save_button', _('Save'), css_class="btn btn-primary"),
                Submit('cancel_button', _('Cancel'), css_class="btn btn-link"),
            )
        )
