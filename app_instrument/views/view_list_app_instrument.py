from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView
from app_instrument.models import AppInstrument
from message_private.models import MessagePrivate
from notifications.models import Notifications


class AppInstrumentListView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, ListView):
    model = AppInstrument
    template_name = 'app_instrument/list_app_instrument.html'
    paginate_by = 15
    permission_required = 'app_instrument.view_AppInstrument'
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

        context['notifications_private_messages'] = MessagePrivate.objects.filter(
            recipient_message__pk=self.request.user.id, flag_read_recipient=False)
        context['count_private_messages'] = MessagePrivate.objects.filter(recipient_message__pk=self.request.user.id,
                                                                          flag_read_recipient=False).count()
        context['notifications'] = Notifications.objects.filter(activated=True)

        context['total_register'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        # Get Params Search
        
        search_instrument_name = self.request.GET.get('search_instrument_name', None)
        search_description = self.request.GET.get('search_description', None)
        search_status = self.request.GET.get('search_status', None)
        
        
        self.request.session['search_instrument_name'] = ''

        self.request.session['search_description'] = ''

        self.request.session['search_status'] = ''

        queryset = AppInstrument.objects.all().order_by('created_at')

        if search_instrument_name:
            self.request.session['search_instrument_name'] = search_instrument_name
            queryset = queryset.filter(instrument_name__icontains=search_instrument_name)

        if search_description:
            self.request.session['search_description'] = search_description
            queryset = queryset.filter(description__icontains=search_description)

        if search_status:
            self.request.session['search_status'] = search_status
            queryset = queryset.filter(status=search_status)

        return queryset