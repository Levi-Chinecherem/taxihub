from django import forms
from .models import Taxi

class TaxiForm(forms.ModelForm):
    class Meta:
        model = Taxi
        fields = ['plate_number', 'model', 'is_available', 'image']

        widgets = {
            'plate_number': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'model': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-checkbox mt-1 block'}),
            'image': forms.FileInput(attrs={'class': 'form-input mt-1 block w-full border-gray-300'}),
        }
