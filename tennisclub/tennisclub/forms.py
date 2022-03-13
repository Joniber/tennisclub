from django import forms
from . import models

class TermineForm(forms.ModelForm):
    class Meta:
        model = models.Termine
        fields = ('bezeichnung', 'date', 'time', 'location',)

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = ('titel', 'inhalt', 'date', 'bild', 'standort',)