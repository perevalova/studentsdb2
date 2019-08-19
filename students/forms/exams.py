
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from students.models import Exam, ExamResults

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions, AppendedText

from django.utils.translation import ugettext as _


class ExamAddForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ExamAddForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('exams_add')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10 exam-form-width'

        self.helper.layout = Layout(
            'subject', 'teacher_first_name', 'teacher_last_name', 'teacher_middle_name', 'date', 'exam_group',
            FormActions(
                Submit('add_button', _('Add'), css_class="btn btn-primary"),
                Submit('cancel_button', _('Cancel'), css_class="btn btn-link"),
            )
        )

        self.helper.layout[4] = Layout(
            AppendedText('date', '<span class="glyphicon glyphicon-calendar"></span>', active=True)
        )


class ExamUpdateForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # call original initializer
        super(ExamUpdateForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper(self)

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('exams_edit', kwargs={'pk': kwargs['instance'].id})

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10 exam-form-width'

        self.helper.layout = Layout(
            'subject', 'teacher_first_name', 'teacher_last_name', 'teacher_middle_name', 'date', 'exam_group',
            FormActions(
                Submit('add_button', _('Save'), css_class="btn btn-primary"),
                Submit('cancel_button', _('Cancel'), css_class="btn btn-link"),
            )
        )

        self.helper.layout[4] = Layout(
            AppendedText('date', '<span class="glyphicon glyphicon-calendar"></span>', active=True)
        )
