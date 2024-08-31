

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def friedList(request):
    return HttpResponse("THis is my Friend List!!!!!!!!")


