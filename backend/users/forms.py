from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
import re

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configuração dos placeholders e classes para cada campo
        self.fields['username'].widget.attrs.update({
            'class': 'mt-1 p-2 w-full border border-cyan-200 rounded shadow-sm focus:outline-none focus:shadow-[0px_2px_20px_rgba(0,0,0,0.3)]',
            'placeholder': 'Nome de usuário'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'mt-1 p-2 w-full border border-cyan-200 rounded shadow-sm focus:outline-none focus:shadow-[0px_2px_20px_rgba(0,0,0,0.3)]',
            'placeholder': 'Email'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'mt-1 p-2 w-full border border-cyan-200 rounded shadow-sm focus:outline-none focus:shadow-[0px_2px_20px_rgba(0,0,0,0.3)]',
            'placeholder': 'Senha'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'mt-1 p-2 w-full border border-cyan-200 rounded shadow-sm focus:outline-none focus:shadow-[0px_2px_20px_rgba(0,0,0,0.3)]',
            'placeholder': 'Confirme sua senha'
        })

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise forms.ValidationError("O email não tem um formato válido")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Esse email já está em uso.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError("O nome de usuário deve ter pelo menos 4 caracteres.")
        if not re.match(r'^[\w]+$', username):
            raise forms.ValidationError("O nome de usuário só pode conter letras, números e underscores.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2:
            if password1 != password2:
                self.add_error('password2', "As senhas não coincidem.")
            elif len(password1) < 8:
                self.add_error('password1', "A senha deve ter no mínimo 8 caracteres.")

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'mt-1 p-2 w-full border border-cyan-200 rounded shadow-sm focus:outline-none focus:shadow-[0px_2px_20px_rgba(0,0,0,0.3)]',
            'placeholder': 'Nome de usuário'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'mt-1 p-2 w-full border border-cyan-200 rounded shadow-sm focus:outline-none focus:shadow-[0px_2px_20px_rgba(0,0,0,0.3)]',
            'placeholder': 'Sua senha'
        })

    error_messages = {
        'invalid_login': _("Usuário ou senha incorretos."),
        'inactive': _("Esta conta está inativa."),
    }