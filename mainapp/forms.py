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
            'class': 'form-control',
            'rows': 3
        })
    )
    status = forms.ChoiceField(label="Статус", choices=CHOICES, initial=1, widget=forms.Select(attrs={
        'class': 'form-select',
    }))


class NewClientForm(forms.Form):
    name = forms.CharField(label="ФИО", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(label="Контакт", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    where_from = forms.CharField(label="Источник заказа", required=False, max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    oder_details = forms.CharField(label="Индивидуальные условия заказа", required=False, max_length=200,
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control'
                                   }))
    address = forms.CharField(label="Адрес доставки", max_length=200, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
    }))
    notes = forms.CharField(label="Заметки", required=False, max_length=200, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
    }))


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
