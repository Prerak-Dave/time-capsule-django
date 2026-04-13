from django.test import TestCase
from tc_auth.forms import *
from django.core.exceptions import ValidationError

class FormsTest(TestCase):
    '''
        Class to test the forms in the app
    '''
    def test_user_signin_form(self):
        '''
            Testing if form gets saved on correct input
        '''
        payload = {
            'email': 'dj@jmail.com',
            'password1': 'Dj@123456',
            'password2': 'Dj@123456'
        }
        
        usersigninform = UserSignin(payload)
        user = usersigninform.save()
        
        self.assertEquals(user.email,'dj@jmail.com')
    
    def test_user_signin_form_errors(self):
        '''
            Testing if form throws error on incorrect input
        '''
        payload = {
            'email': 'dj@gmail.com', #gmail instead of jmail
            'password1': 'Dj@123456',
            'password2': 'Dj@123456'
        }
        
        usersigninform = UserSignin(payload)
        
        self.assertFalse(usersigninform.is_valid())

        self.assertIn('email', usersigninform.errors)
        self.assertEqual(usersigninform.errors['email'], ["Please use a jmail account"])