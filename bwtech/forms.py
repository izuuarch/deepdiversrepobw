from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name*'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name*'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address*'}),
            'message': forms.Textarea(attrs={'placeholder': 'How can we help you?*'}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email']

