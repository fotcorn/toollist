from django.contrib import admin
from toollist.models import Machine, Tool, ToolCooling, ToolEntry, ToolType, ToolHolder

admin.site.register(Machine)
admin.site.register(Tool)
admin.site.register(ToolCooling)
admin.site.register(ToolType)
admin.site.register(ToolHolder)
