from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'password1', 'password2', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None

class CustomRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'confirm_password', 'email']

    def clean_password1(self):# clean_*field-name*
        print('clean running')
        p1 = self.cleaned_data.get('password1')

        if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', p1):
            'NOTE: ValidationError can accept a string and list also dict'
            raise forms.ValidationError('password must include Uppercase, lowercase, number and special charecter')
        
        return p1 # NOTE: cummon error

    def clean(self):
        '''
        NOTE: ultrimately i can use this function for both field and non-field
        '''
        cleaned_data = self.cleaned_data
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('confirm_password')

        if p1!=p2:
            raise forms.ValidationError('password do not match')
        
        return cleaned_data