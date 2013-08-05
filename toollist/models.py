from django.db import models
from django.utils.translation import ugettext_lazy as _

from smart_selects.db_fields import ChainedForeignKey

class ToolType(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Tool type')
        verbose_name_plural = _('Tool types')

class Tool(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(ToolType, verbose_name=_('Tool type'))
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Tool')
        verbose_name_plural = _('Tools')
        
class ToolHolder(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Tool holder')
        verbose_name_plural = _('Tool holders')
    
class ToolCooling(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Tool cooling')
        verbose_name_plural = _('Tool coolings')
    
class Machine(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Machine')
        verbose_name_plural = _('Machines')

class ToolEntry(models.Model):
    number = models.PositiveIntegerField(_('Number'))
    
    type = models.ForeignKey(ToolType, verbose_name=_('Tool type'))
    tool = ChainedForeignKey(Tool, chained_field='type', chained_model_field='type', verbose_name=_('Tool'))
    
    machine = models.ForeignKey(Machine, verbose_name=_('Machine'))
    holder = models.ForeignKey(ToolHolder, verbose_name=_('Holder'))
    cooling = models.ForeignKey(ToolCooling, verbose_name=_('Cooling'))
    
    diameter = models.CharField(_('Diameter'), max_length=10, null=True, blank=True)
    angle = models.PositiveIntegerField(_('Angle'), null=True, blank=True)
    
    pliers = models.DecimalField(_('Pliers'), max_digits=10, decimal_places=1, null=True, blank=True)
    length = models.DecimalField(_('Length'), max_digits=10, decimal_places=3, null=True, blank=True)
    radius = models.DecimalField(_('Radius'), max_digits=10, decimal_places=3, null=True, blank=True)

    class Meta:
        verbose_name = _('Tool entry')
        verbose_name_plural = _('Tools entries')
        unique_together = ('number', 'machine')
    