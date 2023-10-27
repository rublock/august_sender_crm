from django import forms
from .models import Client, Order


class NewOrderForm(forms.Form):
    CHOICES = [
        (1, 'Поступил'),
        (2, 'Собран'),
        (3, 'Отправлен'),
        (4, 'Срочно')
    ]

    client = forms.ModelChoiceField(label="Клиент", queryset=Client.objects.all(), widget=forms.Select(attrs={
        'class': 'form-select',
    }))
    product = forms.CharField(label="Продукт", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(label="Количество", initial=1, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    description = forms.CharField(
        label="Примечание", max_length=200, required=False, widget=forms.Textarea(attrs={
            'class': 'form-control', 'rows': 3
        })
    )
    status = forms.ChoiceField(label="Статус", choices=CHOICES, initial=1, widget=forms.Select(attrs={
        'class': 'form-select',
    }))
