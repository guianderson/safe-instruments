import os
import uuid
from django.db import models

from config_departament.models import ConfigDepartament
from sys_audit.models import SysAudit


class AppInstrument(SysAudit):
        
    instrument_status = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
    )

    # Fields
    instrument_name = models.CharField(max_length=45, verbose_name='Instrumento', null=False, blank=False)
    description = models.CharField(max_length=255, verbose_name='Descrição', null=False, blank=False)    
    department = models.ForeignKey(ConfigDepartament, on_delete=models.CASCADE, verbose_name='Departamento', null=True)
    status = models.CharField(max_length=12, default='Ativo', choices=instrument_status, verbose_name='Situação')
    location = models.CharField(max_length=255, verbose_name='Localização', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    # EndFields

    # META CLASS
    class Meta:
        db_table = 'app_instrument'
        unique_together = ['instrument_name', 'description']
        ordering = ['instrument_name']
        verbose_name = 'Instrumentos'
        verbose_name_plural = 'Instrumentos'

    # TO STRING METHOD
    def __str__(self):
        return '%s | %s' % (self.instrument_name, self.description)
