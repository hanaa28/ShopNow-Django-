from django import forms
from category.models import Category

class ProductForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    image = forms.ImageField(required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    category=forms.ChoiceField(choices=Category.get_all_tracks())