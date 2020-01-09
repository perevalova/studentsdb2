from django.urls import reverse
from django.forms import ModelForm, ValidationError

from students.models import Student, Group

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions, AppendedText


from django.utils.translation import ugettext as _


class StudentAddForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'student_group', 'ticket', 'notes']

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(StudentAddForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('students_add')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10 student-form-width'

        self.helper.layout = Layout(
            'first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'student_group', 'ticket', 'notes',
            FormActions(
                Submit('add_button', _('Save'), css_class="btn btn-primary"),
                Submit('cancel_button', _('Cancel'), css_class="btn btn-link"),
            )
        )
        self.helper.layout[3] = Layout(
            AppendedText('birthday', '<span class="glyphicon glyphicon-calendar"></span>', active=True),
        )

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'student_group', 'ticket', 'notes']

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('students_edit', kwargs={'pk': kwargs['instance'].id})

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10 student-form-width'

        self.helper.layout = Layout(
            'first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'student_group', 'ticket', 'notes',
            FormActions(
                Submit('add_button', _('Save'), css_class="btn btn-primary"),
                Submit('cancel_button', _('Cancel'), css_class="btn btn-link"),
            )
        )
        self.helper.layout[3] = Layout(
            AppendedText('birthday', '<span class="glyphicon glyphicon-calendar"></span>', active=True),
        )

    def clean_student_group(self):
        """Check if student is leader in any group.
        If yes, then ensure it`s the same as selected group."""

        group = Group.objects.filter(leader=self.instance)
        if len(group) > 0 and self.cleaned_data['student_group'] != group[0]:
            raise ValidationError(_('Student is a leader of different group.'), code='invalid')

        return self.cleaned_data['student_group']

