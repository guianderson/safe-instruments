from django.forms import ModelForm, TextInput

from authentication.models import User


class UpdateProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone", "mobile", "avatar",]
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
            'mobile': TextInput(attrs={'class': 'form-control', 'id': 'mobile'}),
        }
        labels = {
            'cpf': ('CPF'),
            'first_name': ('Nome'),
            'last_name': ('Sobrenome'),
            'email': ('E-mail'),
            'phone': ('Telefone'),
            'mobile': ('Celular'),
            'avatar': ('Foto'),
        }
            