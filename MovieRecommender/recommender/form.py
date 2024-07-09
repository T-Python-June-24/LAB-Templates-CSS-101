

from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(label='Enter Movie Title', max_length=100)
