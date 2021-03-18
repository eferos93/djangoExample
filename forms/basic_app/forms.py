from django import forms
from django.core import validators


# CREATE A FORM ------------------------------------------------------
# custom validation function: the argument name must be be 'value'
def check_for_z(value):
    if value[0].lower != 'z':
        raise forms.ValidationError("Name needs to start with z")


class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    # bot_catcher = forms.CharField(required=False,
    #                               widget=forms.HiddenInput,
    #                               validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()  # cleans all data
        # now do custom stuff
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']

        if email != v_email:
            raise forms.ValidationError('Make sure emails match')
    # # this method is overridden
    # Manually validate form field
    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError('GOTCHA BOT!')
    #     return bot_catcher
# --------------------------------------------------------------------------------

# CREATE A FORM FROM AN EXISTING MODEL
