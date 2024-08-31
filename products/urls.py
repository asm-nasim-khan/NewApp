from django.contrib import admin
from django.urls import path


from . import views


urlpatterns = [
    path('productList', views.show_products, name='products'),
    path('signup_add', views.signup_add, name='signup_add'),
]