from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from account.forms import UpdateProfileForm
from message_private.models import MessagePrivate
from notifications.models import Notifications


@login_required
def UpdateProfileView(request):
    breadcumb_app = 'Usuário'
    breadcumb_module = 'Perfil'

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
        form = UpdateProfileForm(request.POST, request.FILES,
                                 instance=request.user)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.actual_user = request.user

            if (request.POST.get('avatar-clear')):
                temp.avatar = None
            temp.save()

            messages.success(request, 'Seu perfil foi atualizado!')
        else:
            messages.error(request, 'Não foi possível atualizar seu perfil.')

    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'account/view_update_profile.html', {'form': form,
                                                                'notifications_private_messages': notifications_private_messages,
                                                                'notifications': notifications,
                                                                'count_private_messages': count_private_messages,
                                                                'breadcumb_app': breadcumb_app,
                                                                'breadcumb_module': breadcumb_module
                                                                })

            