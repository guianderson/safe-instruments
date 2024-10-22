from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView

from message_private.forms import MessagePrivateForm
from message_private.models import MessagePrivate


class MessagePrivateDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = MessagePrivate
    form_class = MessagePrivateForm
    template_name = 'message_private/detail_message_private.html'
    permission_required = 'message_private.view_messageprivate'
    raise_exception = False

    def handle_no_permission(self):
        messages.error(self.request,
                       'Você não possui privilégio suficiente para executar essa operação.')
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect(reverse_lazy('access_denied'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu_message'] = 'side-menu--active'
        context['breadcumb_app'] = 'Caixa de Entrada'
        context['breadcumb_module'] = 'Mensagens'


        # Private Messages
        context['notifications_private_messages'] = MessagePrivate.objects.filter(
            recipient_message__pk=self.request.user.id, flag_read_recipient=False, flag_trash_recipient=False)
        context['count_private_messages'] = MessagePrivate.objects.filter(recipient_message__pk=self.request.user.id,
                                                                          flag_read_recipient=False,
                                                                          flag_trash_recipient=False).count()
        # ./Private Messages
        count_new_message = MessagePrivate.objects.filter(flag_read_recipient=False, flag_trash_recipient=False,
                                                          flag_soft_excluded_recipient=False,
                                                          recipient_message=self.request.user).count()
        count_read_message = MessagePrivate.objects.filter(flag_read_recipient=True,
                                                           flag_soft_excluded_recipient=False,
                                                           recipient_message=self.request.user).count()
        count_trash_message = MessagePrivate.objects.filter(flag_trash_recipient=True,
                                                            flag_soft_excluded_recipient=False,
                                                            recipient_message=self.request.user).count()
        count_send_message = MessagePrivate.objects.filter(to_message=self.request.user).count()

        context['count_new_message'] = count_new_message
        context['count_read_message'] = count_read_message
        context['count_send_message'] = count_send_message
        context['count_trash_message'] = count_trash_message

        # Read Messages
        MessagePrivate.objects.filter(pk=self.kwargs['pk']).update(flag_read_recipient=True)
        # ./Read Messages
        
        return context

            