from django.forms import *

from app_instrument.models import AppInstrument


class AppInstrumentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppInstrumentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AppInstrument
        fields = ['instrument_name', 'description', 'department', 'status', 'location']
        exclude = ['created_at', 'updated_at', 'operator']
        widgets = {
            'instrument_name': TextInput(attrs={'class': 'form-control', 'type': 'text', 'style': 'width: 100%;'}),
            'description': TextInput(attrs={'class': 'form-control', 'type': 'text', 'style': 'width: 100%;'}),
            'department': Select(attrs={'class': 'tom-select w-full', 'data-placeholder': 'Selecione uma opção','style': 'width: 100%;'}),
            'status': Select(attrs={'class': 'tom-select w-full', 'data-placeholder': 'Selecione uma opção','style': 'width: 100%;'}),
            'location': TextInput(attrs={'class': 'form-control', 'type': 'text', 'style': 'width: 100%;'}),
        }
