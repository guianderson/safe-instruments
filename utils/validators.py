import os

from django.core.exceptions import ValidationError


def message_validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.csv', '.xls', '.xlsx', '.xlsm', '.doc', '.docx', '.ppt', '.pptx', '.ods', '.odt', '.odp',
                        '.pdf', 'jpg', '.png', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Extensão não suportada.')


def service_validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.jpeg', '.png', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Extensão não suportada.')


def csv_validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.csv', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Extensão não suportada.')            
