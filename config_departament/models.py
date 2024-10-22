from django.db import models


# Create your models here.

class ConfigDepartament(models.Model):
    departament = models.CharField(max_length=60, unique=True, verbose_name='Departamento')
    description = models.CharField(max_length=255, verbose_name='Descrição')
    status = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data Cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data Atualização')

    class Meta:
        db_table = 'config_departament'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['pk']

    def __str__(self):
        return '%s' % self.departament

            