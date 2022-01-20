from django.contrib.auth.models import User
from django import forms

class ProfileCreateForm(forms.ModelForm):
    """A form to create new users"""

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email']

        widgets = {
            'password':forms.PasswordInput
        }