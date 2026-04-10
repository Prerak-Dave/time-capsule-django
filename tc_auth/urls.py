from django.contrib import admin
from . import views
from django.urls import include,path

app_name = 'auth'
urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('signin/', views.signin_user, name="signin"),

]
