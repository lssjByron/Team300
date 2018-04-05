from django import forms

class SubmitStocks(forms.Form):
	url = forms.URLField()