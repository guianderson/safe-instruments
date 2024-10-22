from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Select

from authentication.models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control mt-3'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password2'].widget.attrs['class'] = 'form-control mt-3'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Senha'
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'agency', 'departament', 'phone',
                  'mobile', 'password1', 'password2']
        exclude = ['avatar', ]
        widgets = {
            'email': TextInput(
                attrs={'type': 'email', 'maxlenght': 14, 'title': 'Digite seu E-mail', 'class': 'form-control mt-3',
                       'required': True}),
            'first_name': TextInput(
                attrs={'type': 'text', 'maxlenght': 30, 'title': 'Digite seu nome', 'class': 'form-control mt-3', 'required': True}),

            'last_name': TextInput(
                attrs={'type': 'text', 'maxlenght': 150, 'title': 'Digite seu sobrenome', 'class': 'form-control mt-3', 'required': True}),

            'agency': Select(
                attrs={'class': 'form-control mt-3', 'required': True}),

            'departament': Select(
                attrs={'class': 'form-control mt-3', 'required': True}),

            'phone': TextInput(
                attrs={'id': 'phone', 'class': 'form-control mt-3', 'required': True}),

            'mobile': TextInput(
                attrs={'id': 'mobile', 'class': 'form-control mt-3', 'required': True}),
        }
        labels = {
            'cpf': ('CPF'),
            'email': ('E-mail'),
            'first_name': ('Nome'),
            'last_name': ('Sobrenome'),
            'agency': ('Agência'),
            'departament': ('Departamento'),
            'phone': ('Telefone'),
            'mobile': ('Celular'),
            'password1': ('Senha'),
            'password2': ('Confirmar Senha'),
        }            
            