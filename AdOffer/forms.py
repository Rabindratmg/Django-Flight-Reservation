from django import forms
from .models import Flight
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class OfferForm(forms.ModelForm):
    
    class Meta:
        model = Flight
        fields = ['From','To','offer','orginal']
