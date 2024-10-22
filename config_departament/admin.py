from django.contrib import admin

from config_departament.models import ConfigDepartament


# Register your models here.


class ConfigDepartamentAdmin(admin.ModelAdmin):
    list_display = ['departament', 'status', 'get_created_at', 'get_updated_at', ]

    @admin.display(description='Data de Cadastro')
    def get_created_at(self, obj):
        if obj.created_at:
            return obj.created_at.strftime('%d/%m/%Y %H:%M:%S')

    @admin.display(description='Data de Atualização')
    def get_updated_at(self, obj):
        if obj.updated_at:
            return obj.updated_at.strftime('%d/%m/%Y %H:%M:%S')

    # Filters
    search_fields = ['departament', 'description', 'status', ]

    # Paginate per page
    list_per_page = 15  # No of records per page

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'operator', None) is None:
            obj.operator = request.user
        obj.save()


# Register Resources
admin.site.register(ConfigDepartament, ConfigDepartamentAdmin)
            