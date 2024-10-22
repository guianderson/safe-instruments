from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from message_private.models import MessagePrivate
from notifications.models import Notifications


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcumb_app'] = 'Início'
        context['breadcumb_module'] = 'Principal'

        context['active_menu_home'] = 'side-menu--active'
        context['active_mobile_menu_home'] = 'menu--active'

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
            
            