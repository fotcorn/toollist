from django.db import models

from smart_selects.db_fields import ChainedForeignKey

class ToolType(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=255)
    tool_type = models.ForeignKey(ToolType)
    def __unicode__(self):
        return self.name
    
class ToolHolder(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class ToolCooling(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class Machine(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name


class ToolEntry(models.Model):
    number = models.PositiveIntegerField()
    
    tool_type = models.ForeignKey(ToolType)
    #tool = GroupedForeignKey(Tool, 'tool_type')
    
    tool = ChainedForeignKey(Tool, chained_field='tool_type', chained_model_field='tool_type')
    
    
    machine = models.ForeignKey(Machine)
    holder = models.ForeignKey(ToolHolder)
    cooling = models.ForeignKey(ToolCooling)
    
    diameter = models.CharField(max_length=10, null=True, blank=True)
    angle = models.PositiveIntegerField(null=True, blank=True)
    
    pliers = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    length = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    radius = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)

