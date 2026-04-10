from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserLogin(forms.ModelForm):
    class Meta:     
        model = User
        fields = ['email', 'password']

    
    
class UserSignin(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        required = ['email']

    def clean_email(self):
        email =  self.cleaned_data['email']
        if email[-10:] != '@jmail.com':
            raise forms.ValidationError("Please use a jmail account")
        
        return email
