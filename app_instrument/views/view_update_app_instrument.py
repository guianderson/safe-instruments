from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db import IntegrityError
from django.views.generic import UpdateView
from app_instrument.forms import AppInstrumentForm
from app_instrument.models import AppInstrument
from message_private.models import MessagePrivate
from notifications.models import Notifications

class AppInstrumentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AppInstrument
    template_name = 'app_instrument/update_app_instrument.html'
    form_class = AppInstrumentForm
    success_message = 'Atualizado com Sucesso.'
    success_url = reverse_lazy('app_instrument:list')
    permission_required = 'app_instrument.change_AppInstrument'
    raise_exception = False

    def handle_no_permission(self):
        messages.error(self.request, 'Você não possui privilégio suficiente para executar essa operação.')
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect(reverse_lazy('access_denied'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['active_menu_app_instrument'] = 'side-menu--active'
        context['breadcumb_app'] = 'Instrumentos'
        context['breadcumb_module'] = 'Gerenciar Instrumentos'

        context['notifications_private_messages'] = MessagePrivate.objects.filter(recipient_message__pk=self.request.user.id, flag_read_recipient=False)
        context['count_private_messages'] = MessagePrivate.objects.filter(recipient_message__pk=self.request.user.id, flag_read_recipient=False).count()

        context['notifications'] = Notifications.objects.filter(activated=True)

        return context

    def form_valid(self, form):
        try:
            form.instance.operator = self.request.user
            return super(AppInstrumentUpdateView, self).form_valid(form)
        except IntegrityError:
            messages.add_message(self.request, messages.ERROR, 'Não é possível inserir registros em duplicidade!')
        return redirect(reverse_lazy('app_instrument:list'))
        