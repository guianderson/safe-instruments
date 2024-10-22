
from django.urls import path

from message_private.views import MessagePrivateListView, MessagePrivateCreateView, MessagePrivateDetailView,     MessagePrivateDeleteView, MessageSendPrivateListView, MessageSendPrivateDetailView, MessageReadPrivateListView,     MessageReadPrivateDetailView, MessageTrashPrivateListView, MessagePrivateUpdateView, MessagePrivateReplyCreateView,     MessagePrivateSoftDeleteUpdateView, MessagePrivateRestoreUpdateView, CleanMessagePrivateRedirectView

app_name = 'message_private'

urlpatterns = [
    path('', MessagePrivateListView.as_view(), name='list'),
    path('create/', MessagePrivateCreateView.as_view(), name='create'),
    path('create/reply/<str:pk>', MessagePrivateReplyCreateView.as_view(), name='create_reply'),
    path('detail/<str:pk>', MessagePrivateDetailView.as_view(), name='detail'),
    path('delete/<str:pk>', MessagePrivateDeleteView.as_view(), name='delete'),
    path('list/send', MessageSendPrivateListView.as_view(), name='list_send'),
    path('detail/send/<str:pk>', MessageSendPrivateDetailView.as_view(), name='detail_send'),
    path('list/read', MessageReadPrivateListView.as_view(), name='list_read'),
    path('list/trash', MessageTrashPrivateListView.as_view(), name='list_trash'),

    path('detail/read/<str:pk>', MessageReadPrivateDetailView.as_view(), name='detail_read'),
    path('update/trash/<str:pk>', MessagePrivateUpdateView.as_view(), name='update_trash'),
    path('update/restore/<str:pk>', MessagePrivateRestoreUpdateView.as_view(), name='update_restore'),
    path('update/trash/remove/<str:pk>', MessagePrivateSoftDeleteUpdateView.as_view(), name='update_trash_remove'),
    path('trash/clean/', CleanMessagePrivateRedirectView.as_view(), name='update_trash_clean'),

]
    