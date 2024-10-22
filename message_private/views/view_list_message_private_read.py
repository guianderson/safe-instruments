from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView

from message_private.models import MessagePrivate


class MessageReadPrivateListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = MessagePrivate
    paginate_by = 15
    template_name = 'message_private/list_message_read_private.html'
    permission_required = 'message_private.view_messageprivate'
    raise_exception = False

    def handle_no_permission(self):
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

    def get_queryset(self):
        search = self.request.GET.get('tf_search', None)
        queryset = MessagePrivate.objects.filter(recipient_message=self.request.user,
                                                 flag_read_recipient=True).order_by('-updated_at')
        if search:
            queryset = MessagePrivate.objects.filter(recipient_message=self.request.user, flag_read_recipient=True,
                                                     subject__icontains=search).order_by(
                '-updated_at') | MessagePrivate.objects.filter(recipient_message=self.request.user,
                                                               flag_read_recipient=True,
                                                               to_message__first_name__icontains=search).order_by(
                '-updated_at') | MessagePrivate.objects.filter(recipient_message=self.request.user,
                                                               flag_read_recipient=True,
                                                               to_message__last_name__icontains=search).order_by(
                '-updated_at') | MessagePrivate.objects.filter(recipient_message=self.request.user,
                                                               flag_read_recipient=True,
                                                               to_message__email__icontains=search).order_by(
                '-updated_at')

        return queryset

            