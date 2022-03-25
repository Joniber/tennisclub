import django_filters
from django_filters import DateRangeFilter
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

    titel = django_filters.CharFilter(field_name='titel', lookup_expr='icontains')
    inhalt = django_filters.CharFilter(field_name='inhalt', lookup_expr='icontains')
    autor = django_filters.CharFilter(field_name='autor__username', lookup_expr='iexact')
    date = DateRangeFilter(field_name='date', empty_label='Gesamter Zeitraum')
    sort = django_filters.ChoiceFilter(choices = CHOICES, method='filter_by_order',empty_label=None, )

    class Meta:
        model = BlogPost
    
        
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
    
    def filter_by_order(self, queryset, name, value):
        if value=='old-new':
            expression = 'date'
        elif value == 'new-old':
            expression = '-date'
        elif value == 'a-z':
            expression = '-body'
        elif value == 'z-a':
            expression = '-body'
        else:
            expression = '-date'
        
        return queryset.order_by(expression)
