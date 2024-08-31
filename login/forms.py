from django import forms
from .models import User

class UserEntry(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname','lname','email','password']