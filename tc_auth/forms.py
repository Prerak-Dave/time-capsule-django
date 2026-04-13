from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate


class UserLogin(forms.Form):  
        
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={"class": "form-control"})
    )
        
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = authenticate(username = email, password = password)

        if not user:
            raise forms.ValidationError("Incorrect credentials")
        
        self.user = user
        return cleaned_data


    
    
class UserSignin(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']
        required = ['email']

    def clean_email(self):
        email =  self.cleaned_data['email']
        if email[-10:] != '@jmail.com':
            raise forms.ValidationError("Please use a jmail account")
        
        return email
