from django import forms
from django.forms import fields

from .models import Book , EmployeeDetails , ManagerDetails

from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'cover', 'price')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'