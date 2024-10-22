from django.db import models

from core import settings


# Create your models here.


class SysAudit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.PROTECT,
                                 verbose_name='Usuário',
                                 editable=False)

    class Meta:
        abstract = True
        