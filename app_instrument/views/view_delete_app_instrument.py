from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import DeleteView
from app_instrument.models import AppInstrument
from message_private.models import MessagePrivate
from notifications.models import Notifications

class AppInstrumentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = AppInstrument
    template_name = 'app_instrument/delete_app_instrument.html'
    success_message = 'Removido com Sucesso.'
    success_url = reverse_lazy('app_instrument:list')
    permission_required = 'app_instrument.delete_AppInstrument'
    raise_exception = False

    def handle_no_permission(self):
        messages.error(self.request, 'Você não possui privilégio suficiente para executar essa operação.')
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect(reverse_lazy('access_denied'))

    def form_valid(self, form):
        try:
            self.object.delete()
            messages.success(self.request, self.success_message)
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(self.request, "Não foi possível excluir o item selecionado porque ele está sendo referenciado por outros registros.")
            return redirect(self.success_url)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.form_valid(None)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_menu_app_instrument'] = 'side-menu--active'
        context['breadcumb_app'] = 'Instrumentos'
        context['breadcumb_module'] = 'Gerenciar Instrumentos'
        context['notifications_private_messages'] = MessagePrivate.objects.filter(recipient_message__pk=self.request.user.id, flag_read_recipient=False)
        context['count_private_messages'] = MessagePrivate.objects.filter(recipient_message__pk=self.request.user.id, flag_read_recipient=False).count()
        context['notifications'] = Notifications.objects.filter(activated=True)
        return context