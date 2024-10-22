from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from message_private.models import MessagePrivate
from notifications.models import Notifications



class AccessDeniedView(LoginRequiredMixin, TemplateView):
    template_name = 'access_denied/access_denied.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcumb_app'] = 'Permissão'
        context['breadcumb_module'] = 'Acesso'

        # Private Messages
        context['notifications_private_messages'] = MessagePrivate.objects.filter(
            recipient_message__pk=self.request.user.id, flag_read_recipient=False)
        context['count_private_messages'] = MessagePrivate.objects.filter(recipient_message__pk=self.request.user.id,
                                                                          flag_read_recipient=False).count()
        # ./Private Messages
        
        # Notifications
        context['notifications'] = Notifications.objects.filter(activated=True)
        # ./Notifications

        return context
          
                    