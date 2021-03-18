from django import forms
from models_exercise.models import User


class NewUserForm(forms.ModelForm):
    # put validations here
    class Meta:
        model = User  # create a form based on the given model
        fields = '__all__'  # take all fields
