
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from message_private.models import MessagePrivate
from notifications.models import Notifications


@login_required
def UpdatePasswordView(request):
    breadcumb_app = 'Usuário'
    breadcumb_module = 'Alterar Senha'

    # Private Messages
    notifications_private_messages = MessagePrivate.objects.filter(
        recipient_message__pk=request.user.id, flag_read_recipient=False)
    count_private_messages = MessagePrivate.objects.filter(recipient_message__pk=request.user.id,
                                                                      flag_read_recipient=False).count()
    # ./Private Messages
    
    # Notifications    
    notifications = Notifications.objects.filter(activated=True)
    # ./Notifications

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Sua senha foi atualizada!')
        else:
            messages.error(request,
                           'Não foi possível alterar sua senha. Verifique'
                           ' se sua senha atual ou a confirmação da nova senha '
                           'estão corretas.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/view_update_password.html', {'form': form,
                                                                 'notifications_private_messages': notifications_private_messages,
                                                                 'notifications': notifications,
                                                                 'count_private_messages': count_private_messages,
                                                                 'breadcumb_app': breadcumb_app,
                                                                 'breadcumb_module': breadcumb_module})

            