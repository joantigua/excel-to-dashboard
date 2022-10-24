from importlib import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *
from import_export import resources
# Register your models here.

class AgentResource(resources.ModelResource):
    class Meta:
        model = Agent
        fields = ('agent_id', 'name', 'qa', 'ce', 'csat', 'aht', 'hc')

class AgentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('agent_id', 'name', 'qa', 'ce', 'csat', 'aht', 'hc')
    pass


admin.site.register(Agent, AgentAdmin)