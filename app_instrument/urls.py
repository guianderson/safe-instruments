
from django.urls import path

from app_instrument.views.view_create_app_instrument import AppInstrumentCreateView
from app_instrument.views.view_delete_app_instrument import AppInstrumentDeleteView
from app_instrument.views.view_delete_selected_app_instrument import AppInstrumentDeleteSelectedView
from app_instrument.views.view_detail_app_instrument import AppInstrumentDetailView
from app_instrument.views.view_list_app_instrument import AppInstrumentListView
from app_instrument.views.view_update_app_instrument import AppInstrumentUpdateView

app_name = 'app_instrument'

urlpatterns = [
    path('home/', AppInstrumentListView.as_view(), name='list'),
    path('detail/<int:pk>', AppInstrumentDetailView.as_view(), name='detail'),
    path('create/', AppInstrumentCreateView.as_view(), name='create'),
    path('update/<int:pk>', AppInstrumentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AppInstrumentDeleteView.as_view(), name='delete'),
    path('delete/selected/', AppInstrumentDeleteSelectedView.as_view(), name='delete-selected'),
    ] 
        