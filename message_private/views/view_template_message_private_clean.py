from django.views.generic import RedirectView

from message_private.models import MessagePrivate


class CleanMessagePrivateRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'message_private:list_trash'

    def get_redirect_url(self, *args, **kwargs):
        MessagePrivate.objects.filter(recipient_message=self.request.user.pk, flag_trash_recipient=True).update(
            flag_soft_excluded_recipient=True)
        return super(CleanMessagePrivateRedirectView, self).get_redirect_url(*args, **kwargs)
            