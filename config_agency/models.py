from django.db import models


# Create your models here.
class ConfigAgency(models.Model):
    agency = models.CharField(max_length=60, unique=True, verbose_name='Organização')
    description = models.CharField(max_length=255, verbose_name='Descrição')
    status = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data Cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data Atualização')

    class Meta:
        db_table = 'config_agency'
        verbose_name = 'Organização'
        verbose_name_plural = 'Organizações'
        ordering = ['pk']

    def __str__(self):
        return '%s' % self.agency
