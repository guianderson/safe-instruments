from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from message_private.models import MessagePrivate


class MessagePrivateDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = MessagePrivate
    template_name = 'message_private/delete_message_private.html'
    success_message = 'Mensagem Removida com Sucesso.'
    success_url = reverse_lazy('message_private:list')
    permission_required = 'message_private.delete_messageprivate'
    raise_exception = False

    def handle_no_permission(self):
        messages.error(self.request, 'Você não possui privilégio suficiente para executar essa operação.')
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

        return context

    def delete(self, request, *args, **kwargs):
        try:
            verify_message_read = MessagePrivate.objects.filter(pk=self.kwargs['pk'], flag_read_recipient=False)
            if verify_message_read:
                messages.success(self.request, self.success_message)
                return super(MessagePrivateDeleteView, self).delete(request, *args, **kwargs)
            else:
                messages.add_message(request, messages.ERROR,
                                     'Não é possível remover mensagens que já foram lidas pelo destinatário.')
                return redirect(reverse_lazy('message_private:list'))

        except ProtectedError:
            messages.add_message(request, messages.ERROR,
                                 'Operação de remoção cancelada. Ele está sendo usado por outros módulos')
            return redirect(reverse_lazy('message_private:list'))
            