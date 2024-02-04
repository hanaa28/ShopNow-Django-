from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
   