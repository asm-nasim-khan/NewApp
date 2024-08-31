from django import forms
from .models import Product

class ProductEntry(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','describe','price']