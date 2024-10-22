from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from message_private.forms import MessagePrivateCreateRepyForm
from message_private.models import MessagePrivate


class MessagePrivateReplyCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = MessagePrivate
    template_name = 'message_private/create_message_private_reply.html'
    form_class = MessagePrivateCreateRepyForm
    success_message = 'Mensagem Enviada com Sucesso.'
    success_url = reverse_lazy('message_private:list')
    permission_required = 'message_private.add_messageprivate'
    raise_exception = False

    def handle_no_permission(self):
        messages.error(self.request, 'Você não possui privilégios suficientes para acessar esse módulo.')
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect(reverse_lazy('access_denied'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu_message'] = 'side-menu--active'
        context['breadcumb_app'] = 'Caixa de Entrada'
        context['breadcumb_module'] = 'Mensagens'

        # Private Messages
        context['notifications_private_messages'] = MessagePrivate.objects.filter(
            recipient_message__pk=self.request.user.id, flag_read_recipient=False)
        context['count_private_messages'] = MessagePrivate.objects.filter(recipient_message__pk=self.request.user.id,
                                                                          flag_read_recipient=False).count()
        # ./Private Messages
        return context

    def form_valid(self, form):
        messages_private = MessagePrivate.objects.filter(pk=self.kwargs['pk'])
        for message in messages_private:
            to_message = message.to_message.pk
            recipient_message = message.recipient_message.pk
            subject = message.subject
        try:
            form.instance.subject = 'Re: ' + subject
            form.instance.recipient_message_id = to_message
            form.instance.to_message_id = recipient_message

            return super(MessagePrivateReplyCreateView, self).form_valid(form)
        except IntegrityError:
            messages.add_message(self.request, messages.ERROR, 'Não é possível inserir registros em duplicidade!')
            return redirect(reverse_lazy('message_private:list'))
 
            