from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from message_private.forms import MessagePrivateForm, MessagePrivateUpdateTrashForm
from message_private.models import MessagePrivate


class MessagePrivateUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = MessagePrivate
    form_class = MessagePrivateUpdateTrashForm
    template_name = 'message_private/update_message_trash_private.html'
    success_message = "Enviado para Lixeira."
    success_url = reverse_lazy('message_private:list')
    permission_required = 'message_private.change_messageprivate'
    raise_exception = False

    def handle_no_permission(self):
        messages.error(self.request,
                       'Você não possui privilégio suficiente para executar essa operação.')
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect(reverse_lazy('message_private:list'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcumb_app'] = 'Caixa de Entrada'
        context['breadcumb_module'] = 'Mensagens'
        return context

    def form_valid(self, form):
        try:
            form.instance.flag_trash_recipient = True
            return super(MessagePrivateUpdateView, self).form_valid(form)
        except IntegrityError:
            messages.add_message(self.request, messages.ERROR,
                                 'Não é possível inserir registros em duplicidade!')
            return redirect(reverse_lazy('message_private:list'))

            