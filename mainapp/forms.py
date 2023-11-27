from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django_summernote.widgets import SummernoteWidget

from .models import Client, Order, OrderPosition


class NewOrderForm(forms.Form):
    CHOICES = [
        (1, 'Поступил'),
        (2, 'Собран'),
        (3, 'Отправлен'),
        (4, 'Срочно')
    ]

    client = forms.CharField(label="Клиент", max_length=100)
    description = forms.CharField(required=True,
                                  widget=SummernoteWidget(
                                      attrs={'summernote': {
                                          'width': '100%',
                                          'height': '300px'
                                      }
                                      }))
    track_number = forms.CharField(label="Трэк №", required=False, max_length=50)
    status = forms.ChoiceField(label="Статус", choices=CHOICES, initial=1)


class ChangeOrderForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {
        'width': '100%',
        'height': '300px'
    }
    }))

    class Meta:
        model = OrderPosition
        fields = ['client', 'description', 'track_number', 'status']

        widgets = {
            'client': forms.Select(attrs={'class': 'form-select', }),
            'description': forms.Textarea(),
            'track_number': forms.TextInput(attrs={'class': 'form-control', }),
            'status': forms.Select(attrs={'class': 'form-select', }),
        }


class NewClientForm(forms.Form):
    name = forms.CharField(max_length=100)
    contact = forms.CharField(required=False, max_length=200)
    where_from = forms.CharField(required=False, max_length=200)
    oder_details = forms.CharField(required=False, max_length=200)
    address = forms.CharField(required=False, max_length=200)
    notes = forms.CharField(required=False, max_length=200, widget=forms.Textarea)


class ChangeClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'contact', 'where_from', 'oder_details', 'address', 'notes']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'where_from': forms.TextInput(attrs={'class': 'form-control'}),
            'oder_details': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, }),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, }),
        }
