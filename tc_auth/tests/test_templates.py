from django.test import TestCase
from django.template.loader import get_template
from django import forms

class UserLoginForm(forms.Form):
    '''
        Dummy login form containing email and 
        password fields only, styled to bootstrap4.
    '''
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    
class TemplateTests(TestCase):
    '''
        Class to test various templates in tc_auth
    '''
    def test_login_form_template_renders(self):
        '''
            Checks whether login template renders correctly.
        '''
        template = get_template('tc_auth/login.html')
        rendered = template.render({'form':UserLoginForm()})
        
        self.assertIn('<form',rendered)
        self.assertIn("<input type=\"email\"",rendered)
        self.assertIn("<input type=\"password\"",rendered)
        self.assertIn("class=\"form-control",rendered)
        self.assertNotIn("<div class='errors'",rendered)
        
    def test_login_form_template_error_renders(self):
        template = get_template('tc_auth/login.html')
        rendered = template.render({'form':UserLoginForm(),'exception':Exception("Wrong creds")})
        
        self.assertIn('<form',rendered)
        self.assertIn('<p>Wrong',rendered)