from django.urls import path
from .views import generate_instrument_report

app_name = 'app_instrument_log'

urlpatterns = [
    path('relatorio/instrumentos/', generate_instrument_report, name='relatorio_instrumentos'),
]