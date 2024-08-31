from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserEntry

def login(request):
    return render(request, "products/login_page.html", {})

def signup_new(request):
    if request.method == "POST":
        form = UserEntry(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, "login/signup_page.html", {})
    else:
        return render(request, "login/signup_page.html", {})
