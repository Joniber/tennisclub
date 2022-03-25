import django_filters
from django_filters import DateRangeFilter
from matplotlib import widgets
from .models import *
from django import forms
class DateInput(forms.DateInput):
    input_type = 'date'

class BlogFilter(django_filters.FilterSet):

    CHOICES =(
        ('new-old', 'neu->alt'),
        ('old-new', 'alt->neu'),
        ('a-z', 'a->z'),
        ('z-a', 'z->a'),
    )

    titel = django_filters.CharFilter(field_name='titel', lookup_expr='icontains', label="Titel", widget=forms.TextInput(attrs={'placeholder': 'Titel', 'class': 'form-control'}))
    inhalt = django_filters.CharFilter(field_name='inhalt', lookup_expr='icontains', label="Inhalt", widget=forms.TextInput(attrs={'placeholder': 'Inhalt', 'class': 'form-control'}))
    autor = django_filters.CharFilter(field_name='autor__username', lookup_expr='iexact', label="Autor", widget=forms.TextInput(attrs={'placeholder': 'Autor', 'class': 'form-control'}))
    standort = django_filters.CharFilter(field_name='standort', lookup_expr='iexact', label="Standort", widget=forms.TextInput(attrs={'placeholder': 'Standort', 'class': 'form-control'}))

    date = DateRangeFilter(field_name='date', empty_label='Gesamter Zeitraum', label="Datum")
    sort = django_filters.ChoiceFilter(choices = CHOICES, method='filter_by_order',empty_label=None, label="Sortieren")

    class Meta:
        model = BlogPost
        fields = {

        }

    
    def filter_by_order(self, queryset, name, value):
        if value=='old-new':
            expression = 'date'
        elif value == 'new-old':
            expression = '-date'
        elif value == 'a-z':
            expression = 'inhalt'
        elif value == 'z-a':
            expression = '-inhalt'
        else:
            expression = '-date'
        
        return queryset.order_by(expression)

class TerminFilter(django_filters.FilterSet):

    CHOICES =(
        ('new-old', 'neu->alt'),
        ('old-new', 'alt->neu'),
        ('a-z', 'a->z'),
        ('z-a', 'z->a'),
    )

    bezeichnung = django_filters.CharFilter(field_name='bezeichnung', lookup_expr='icontains', label="Titel", widget=forms.TextInput(attrs={'placeholder': 'Titel', 'class': 'form-control'}))
    autor = django_filters.CharFilter(field_name='autor__username', lookup_expr='iexact', label="Autor", widget=forms.TextInput(attrs={'placeholder': 'Autor', 'class': 'form-control'}))
    standort = django_filters.CharFilter(field_name='location', lookup_expr='iexact', label="Standort", widget=forms.TextInput(attrs={'placeholder': 'Standort', 'class': 'form-control'}))

    date = DateRangeFilter(field_name='date', empty_label='Gesamter Zeitraum', label="Datum")
    sort = django_filters.ChoiceFilter(choices = CHOICES, method='filter_by_order',empty_label=None, label="Sortieren")

    class Meta:
        model = BlogPost
        fields = {

        }

    
    def filter_by_order(self, queryset, name, value):
        if value=='old-new':
            expression = 'date'
        elif value == 'new-old':
            expression = '-date'
        elif value == 'a-z':
            expression = 'inhalt'
        elif value == 'z-a':
            expression = '-inhalt'
        else:
            expression = '-date'
        
        return queryset.order_by(expression)