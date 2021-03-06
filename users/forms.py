from django.contrib.auth.models import User
from django import forms
from .models import Profile
class UserCreateForm(forms.ModelForm):
    """A form to create new users"""

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email']

        widgets = {
            'password':forms.PasswordInput
        }



class ProfileCreateForm(forms.ModelForm):
    """A form to create new profile for users"""
    class Meta:
        model = Profile
        fields = ('date_of_birth','profile_photo','bio')
        widget = {
            'birth_date':forms.DateInput(
                format=('%Y-%m-%d',),
                attrs={
                    'type':'date',
                    'placeholder':'Birthday'
                }
            )
        }


class UserEditForm(forms.ModelForm):
    """A form to edit users credentials"""
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')


class ProfileEditForm(forms.ModelForm):
    """A form to edit users profile"""

    class Meta:
        model = Profile
        fields = ('date_of_birth','profile_photo','bio')
        widget = {
            'birth_date':forms.DateInput(
                format=('%Y-%m-%d',),
                attrs={
                    'type':'date',
                    'placeholder':'Birthday'
                }
            )
        }
