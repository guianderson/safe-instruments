from django.db import models

from sys_audit.models import SysAudit


# Create your models here.
class Notifications(SysAudit):
    # CHOICES
    TYPE_CHOICES = (
        ('info', 'Informação'),
        ('warning', 'Aviso'),
        ('danger', 'Atenção'),
    )

    #Fields
    title = models.CharField(max_length=30, verbose_name='Titulo')
    message = models.CharField(max_length=24, verbose_name='Mensagem')
    type = models.CharField(max_length=7, default='info', choices=TYPE_CHOICES, verbose_name='Tipo')
    activated = models.BooleanField(default=True, verbose_name='Ativado')
    #EndFields

    # META CLASS
    class Meta:
        db_table = 'notification'
        ordering = ['title']
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'

    # TO STRING METHOD
    def __str__(self):
        return self.title

            