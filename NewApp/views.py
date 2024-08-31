from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "products/login_page.html", {})


def about(request):
    return HttpResponse("Hello, world! From about!!! ")