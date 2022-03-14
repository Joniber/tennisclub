from django import forms
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class TermineForm(forms.ModelForm):
    class Meta:
        model = models.Termine
        fields = ('bezeichnung', 'date', 'time', 'location',)
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = ('titel', 'inhalt', 'date', 'bild', 'standort',)
        widgets = {
            'date': DateInput(),
        }

class GalerieForm(forms.ModelForm):
    class Meta:
        model = models.Galerie
        fields = ('bild', 'date', 'beschreibung', 'standort')
        widgets = {
            'date': DateInput()
        }