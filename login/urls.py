from django.contrib import admin
from django.urls import path


from . import views


urlpatterns = [
    path('signup', views.signup_new, name='sign_up'),

    path('login_new', views.login, name='login_new'),
]