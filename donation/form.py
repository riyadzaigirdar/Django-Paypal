from django import forms
from donation.models import Donation

class DonationForm(forms.Form):
    name = forms.CharField(max_length=20)
    amount = forms.FloatField()