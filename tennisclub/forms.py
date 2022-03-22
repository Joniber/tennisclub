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
            'date': DateInput(attrs={
                'class': "form-control",
                'placeholder': 'Tag Monat Jahr',
                }),
            'time': TimeInput(attrs={
                'class': "form-control",
               
                }),
            'bezeichnung': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Bezeichnung'
                }),
            'location': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Standort'
                }),

        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = ('titel', 'inhalt', 'date', 'bild', 'standort',)
        widgets = {
            'date': DateInput(attrs={
                'class': "form-control",
                'placeholder': 'Tag Monat Jahr',
                }),
            'bild': forms.FileInput(attrs={
                    'class': "form-control",
                }),
            'standort': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Standort'
                }),
            'inhalt': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Inhalt'
                }),
            'titel': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Titel'
                }),
            
            
        }

class GalerieForm(forms.ModelForm):
    class Meta:
        model = models.Galerie
        fields = ('bild', 'date', 'beschreibung', 'standort')
        widgets = {
            'date': DateInput(attrs={
                'class': "form-control",
                'placeholder': 'Tag Monat Jahr',
                }),
            'beschreibung': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Beschreibung'
                }),
                'standort': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Standort'
                }),
                'bild': forms.FileInput(attrs={
                    'class': "form-control",
                })
        }

class KommentarForm(forms.ModelForm):
    class Meta:
        model = models.Kommentar
        fields = ('autor', 'inhalt', 'email',)
        widgets = {
            
            'autor': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Anzeigename'
                }),
                'inhalt': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Inhalt'
                }),
                'email': forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
                })
        }