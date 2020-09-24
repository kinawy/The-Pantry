from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=30, required=True)
    farm_name = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', required=True)
    location = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=10, required=True)


    class Meta:
        model = User
        fields = ('username', 'full_name', 'farm_name', 'email', 'location', 'phone_number', 'password1', 'password2', )