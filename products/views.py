
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .forms import ProductEntry

def show_products(request):
    all_products = Product.objects.all
    return render(request, "products/show_product.html", {'my_products':all_products})

def signup_add(request):
    if request.method == "POST":
        form = ProductEntry(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, "products/signup_page.html", {})
    else:
        return render(request, "products/signup_page.html", {})

