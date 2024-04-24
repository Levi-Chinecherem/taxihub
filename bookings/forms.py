from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['taxi', 'pickup_time']
        widgets = {
            'taxi': forms.Select(attrs={'class': 'form-select mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'}),
            'pickup_time': forms.DateTimeInput(
                attrs={
                    'class': 'form-input datetimepicker-input mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
                    'data-target': '#datetimepicker1',  # Target for the picker
                    'placeholder': 'Select Pickup Time',
                }
            ),
        }
