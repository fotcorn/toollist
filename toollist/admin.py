from django.contrib import admin
from toollist.models import Machine, Tool, ToolCooling, ToolType, ToolHolder


class ToolHolderAdmin(admin.ModelAdmin):
    list_filter = ('machine',)

admin.site.register(Machine)
admin.site.register(Tool)
admin.site.register(ToolCooling)
admin.site.register(ToolType)
admin.site.register(ToolHolder, ToolHolderAdmin)
