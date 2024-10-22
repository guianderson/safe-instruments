import os
import uuid

from ckeditor.fields import RichTextField
from django.db import models

from authentication.models import User
from core import settings
from utils.validators import message_validate_file_extension


# Create your models here.

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('files_messages_private/', filename)


class MessagePrivate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    to_message = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.PROTECT, editable=False)
    recipient_message = models.ForeignKey(User, on_delete=models.PROTECT, related_name='private_recipient')
    subject = models.CharField(max_length=100, blank=False, null=False, default=None)
    content = RichTextField(default=None)
    attach_1 = models.FileField(upload_to=get_file_path, validators=[message_validate_file_extension], blank=True,
                                null=True)
    attach_2 = models.FileField(upload_to=get_file_path, validators=[message_validate_file_extension], blank=True,
                                null=True)
    attach_3 = models.FileField(upload_to=get_file_path, validators=[message_validate_file_extension], blank=True,
                                null=True)
    attach_4 = models.FileField(upload_to=get_file_path, validators=[message_validate_file_extension], blank=True,
                                null=True)
    flag_read_to = models.BooleanField(default=False, editable=False)
    flag_read_recipient = models.BooleanField(default=False, editable=False)

    flag_trash_to = models.BooleanField(default=False, editable=False)
    flag_trash_recipient = models.BooleanField(default=False, editable=False)
    flag_soft_excluded_to = models.BooleanField(default=False, editable=False)
    flag_soft_excluded_recipient = models.BooleanField(default=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'message_private'
        ordering = ['flag_read_recipient', '-updated_at']

    def __str__(self):
        return '%s' % self.subject


            