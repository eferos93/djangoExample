from django import forms
from django.core import validators


# custom validation function: the argument name must be be 'value'
def check_for_z(value):
    if value[0].lower != 'z':
        raise forms.ValidationError("Name needs to start with z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False,
                                  widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    # # this method is overridden
    # Manually validate form field
    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError('GOTCHA BOT!')
    #     return bot_catcher
