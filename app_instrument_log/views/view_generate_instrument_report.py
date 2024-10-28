import pandas as pd
from django.http import HttpResponse

from app_instrument_log.models import AppInstrumentLog


def generate_instrument_report(request):
    # Consultar todos os registros do modelo AppInstrumentLog
    instruments = AppInstrumentLog.objects.all().values(
        'instrument_id',
        'instrument_name',
        'description',
        'department__departament',
        'status',
        'location',
        'created_at',
        'updated_at'
    )
    
    # Criar um DataFrame com os dados
    df = pd.DataFrame(list(instruments))

    # Renomear as colunas para o relatório
    df.columns = [
        'ID Instrumento',
        'Instrumento',
        'Descrição',
        'Departamento',
        'Situação',
        'Localização',
        'Criado em',
        'Atualizado em'
    ]

    # Gerar um arquivo Excel (ou CSV) como resposta
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=relatorio_instrumentos.xlsx'

    # Criar um ExcelWriter e salvar o DataFrame
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Instrumentos')

    return response