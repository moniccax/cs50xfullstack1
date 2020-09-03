from django import forms
from .models import Product
from . import util

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title',
                    'body'
        ]
    #title = forms.CharField(label="New title")
    #body = forms.CharField(label="New title")
