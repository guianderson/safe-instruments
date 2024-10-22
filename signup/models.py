from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from core import settings


# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL,
          dispatch_uid='projectname.signup.models.user_post_save_handler')
def user_post_save(sender, instance, created, **kwargs):
    """ This method is executed whenever an user object is saved """
    if created:
        pass
        # instance.groups.add(Group.objects.get(name='guest'))

            