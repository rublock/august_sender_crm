from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        "class": "form-control mb-1",
        'placeholder': 'Логин',
    }))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={
        "class": "form-control mb-1",
        'placeholder': 'Пароль',
    }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
