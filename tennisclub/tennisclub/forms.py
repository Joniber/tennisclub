from django import forms
from . import models

class TermineForm(forms.ModelForm):
    class Meta:
        model = models.Termine
        fields = ('bezeichnung', 'date', 'time', 'location',)