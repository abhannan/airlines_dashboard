from django import forms
from .models import Airline, Year

class AirlineForm(forms.Form):
	airline = forms.ModelChoiceField(queryset=Airline.objects.all())