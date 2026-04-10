from django.test import TestCase, Client
from tc_auth.views import *



class SignInUser(TestCase):
    def setup(self):
        self.client = Client()

    def test_signin_user_get(self):
        response = self.client.get("/auth/signin/")
        self.assertEquals(response.status_code, 200)

    def test_signin_user_post(self):
        response = self.client.post("/auth/signin/", {
            "email":"john@jmail.com", 
            "password1":"Simform@123", 
            "password2":"Simform@123"
            })
        self.assertEquals(response.status_code, 200)

        wrong_response = self.client.post("/auth/signin/", {"username":"john", "password":""})
        self.assertNotEquals(wrong_response.status_code, 200)

 

