from django import forms
from apps.products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'picture', 'price', 'amount', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'picture': forms.FileInput(attrs={'class': "form-control"}),
            'price': forms.NumberInput(attrs={'class': "form-control"}),
            'amount': forms.NumberInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': "form-control"}),
        }
