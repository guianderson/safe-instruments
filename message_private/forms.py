from django.forms import ModelForm, Select, TextInput
from message_private.models import MessagePrivate


class MessagePrivateForm(ModelForm):
    class Meta:
        model = MessagePrivate
        fields = ['recipient_message', 'subject', 'content', 'attach_1', 'attach_2', 'attach_3', 'attach_4', 'flag_read_to', 'flag_read_recipient', 'flag_trash_to', 'flag_trash_recipient', 'flag_soft_excluded_to', 'flag_soft_excluded_recipient']
        exclude = ['flag_read_to', 'flag_read_recipient', 'flag_trash_to', 'flag_trash_recipient', 'flag_soft_excluded_to', 'flag_soft_excluded_recipient']

        widgets = {
            'recipient_message': Select(attrs={'class': 'tom-select w-full'}),
            'subject': TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'recipient_message': ('Para'),
            'subject': ('Assunto'),
            'content': ('Mensagem'),
            'attach_1': ('Anexar Arquivo'),
            'attach_2': ('Anexar Arquivo'),
            'attach_3': ('Anexar Arquivo'),
            'attach_4': ('Anexar Arquivo'),
        }


class MessagePrivateUpdateTrashForm(ModelForm):
    class Meta:
        model = MessagePrivate
        fields = ['recipient_message', 'subject', 'content', 'attach_1', 'attach_2', 'attach_3', 'attach_4', 'flag_soft_excluded']
        exclude = ['flag_read', 'recipient_message', 'subject', 'content', 'attach_1', 'attach_2', 'attach_3', 'attach_4', 'flag_soft_excluded']


class MessagePrivateCreateRepyForm(ModelForm):
    class Meta:
        model = MessagePrivate
        fields = ['recipient_message', 'subject', 'content', 'attach_1', 'attach_2', 'attach_3', 'attach_4', ]
        exclude = ['flag_read', 'recipient_message', 'subject',]

        labels = {
            'content': ('Mensagem'),
            'attach_1': ('Anexar Arquivo'),
            'attach_2': ('Anexar Arquivo'),
            'attach_3': ('Anexar Arquivo'),
            'attach_4': ('Anexar Arquivo'),
        }
            