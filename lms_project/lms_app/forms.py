from tkinter import Widget
from django import forms
from .models import Book, Category

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["name"]
        Widget = {
            'name': forms.TextInput(attrs = {'class': 'form-control'})
        }

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'bookPhoto',
            'authorPhoto',
            'pages',
            'price',
            'rentPricePerDay',
            'rentalPeriod',
            'totalRent',
            'status',
            'category',
            ]

        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'author': forms.TextInput(attrs= {'class': 'form-control'}),
            'bookPhoto': forms.FileInput(attrs= {'class': 'form-control'}),
            'authorPhoto': forms.FileInput(attrs= {'class': 'form-control'}),
            'pages': forms.NumberInput(attrs= {'class': 'form-control'}),
            'price': forms.NumberInput(attrs= {'class': 'form-control'}),
            'rentPricePerDay': forms.NumberInput(attrs= {'class': 'form-control', 'id':'rentPrice'}),
            'rentalPeriod': forms.NumberInput(attrs= {'class': 'form-control', 'id':'rentDays'}),
            'totalRent': forms.NumberInput(attrs= {'class': 'form-control', 'id':'totalRentProfit'}),
            'status': forms.Select(attrs= {'class': 'form-control'}),
            'category': forms.Select(attrs= {'class': 'form-control'}),
        }