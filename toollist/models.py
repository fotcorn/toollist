from django.db import models
from django.utils.translation import ugettext_lazy as _

from smart_selects.db_fields import ChainedForeignKey


class ToolType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tool type')
        verbose_name_plural = _('Tool types')
        ordering = ('name',)


class Tool(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(ToolType, verbose_name=_('Tool type'), on_delete=models.CASCADE)

    def __str__(self):
        return u'{0} ({1})'.format(self.name, self.type.name)

    class Meta:
        verbose_name = _('Tool')
        verbose_name_plural = _('Tools')
        ordering = ('type__name', 'name')


class ToolCooling(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tool cooling')
        verbose_name_plural = _('Tool coolings')


class Machine(models.Model):
    MILLING = 1
    TURNING = 2
    TYPE_CHOICES = (
        (MILLING, _('Milling')),
        (TURNING, _('Turning')),
    )

    name = models.CharField(max_length=255)
    type = models.IntegerField(choices=TYPE_CHOICES, default=MILLING)

    def __str__(self):
        return self.name

    def is_milling(self):
        return self.type == Machine.MILLING

    def is_turning(self):
        return self.type == Machine.TURNING

    class Meta:
        verbose_name = _('Machine')
        verbose_name_plural = _('Machines')


class ToolHolder(models.Model):
    name = models.CharField(max_length=255)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    def __str__(self):
        return u'{0} ({1})'.format(self.name, self.machine.name)

    class Meta:
        verbose_name = _('Tool holder')
        verbose_name_plural = _('Tool holders')
        ordering = ('name',)


class ToolEntry(models.Model):

    MACHINE = 1
    CLOSET = 2
    NA = 3
    STATUS_CHOICES = (
        (MACHINE, _('Machine')),
        (CLOSET, _('Closet')),
        (NA, _('NA')),
    )

    number = models.BigIntegerField(_('Number'), blank=True, null=True)

    name = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(ToolType, verbose_name=_('Tool type'), on_delete=models.CASCADE)
    tool = ChainedForeignKey(Tool, chained_field='type', chained_model_field='type', verbose_name=_('Tool'),
                             on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=MACHINE)

    machine = models.ForeignKey(Machine, verbose_name=_('Machine'), on_delete=models.CASCADE)
    holder = models.ForeignKey(ToolHolder, verbose_name=_('Holder'), on_delete=models.CASCADE)
    cooling = models.ForeignKey(ToolCooling, verbose_name=_('Cooling'), on_delete=models.CASCADE)

    diameter = models.CharField(_('Diameter'), max_length=10, null=True, blank=True)
    angle = models.DecimalField(_('Angle'), max_digits=10, decimal_places=2, null=True, blank=True)
    cog_count = models.PositiveIntegerField(_('Cog count'), null=True, blank=True)
    blade_length = models.DecimalField(_('Blade length (Ap)'), max_digits=10, decimal_places=2, null=True, blank=True)
    chip_flute_length = models.DecimalField(_('Chip flute (Apm)'), max_digits=10, decimal_places=2, null=True, blank=True)

    pliers = models.DecimalField(_('Pliers'), max_digits=10, decimal_places=1, null=True, blank=True)
    length = models.DecimalField(_('Length'), max_digits=10, decimal_places=3, null=True, blank=True)
    radius = models.CharField(_('Radius'), max_length=20, null=True, blank=True)
    edge_radius = models.DecimalField(_('Edge radius'), max_digits=10, decimal_places=3, null=True, blank=True)

    comment = models.CharField(_('Comment'), max_length=100, blank=True, null=True)

    geometry_x = models.DecimalField(_('Geomentry X'), max_digits=6, decimal_places=3, null=True, blank=True)
    geometry_z = models.DecimalField(_('Geomentry Z'), max_digits=6, decimal_places=3, null=True, blank=True)
    geometry_r = models.DecimalField(_('Geomentry R'), max_digits=6, decimal_places=3, null=True, blank=True)
    geometry_y = models.DecimalField(_('Geomentry Y'), max_digits=6, decimal_places=3, null=True, blank=True)
    geometry_c = models.DecimalField(_('Geomentry C'), max_digits=6, decimal_places=3, null=True, blank=True)

    wear_x = models.DecimalField(_('Wear X'), max_digits=6, decimal_places=3, null=True, blank=True)
    wear_z = models.DecimalField(_('Wear Z'), max_digits=6, decimal_places=3, null=True, blank=True)
    wear_r = models.DecimalField(_('Wear R'), max_digits=6, decimal_places=3, null=True, blank=True)
    wear_y = models.DecimalField(_('Wear Y'), max_digits=6, decimal_places=3, null=True, blank=True)
    wear_c = models.DecimalField(_('Wear C'), max_digits=6, decimal_places=3, null=True, blank=True)

    class Meta:
        verbose_name = _('Tool entry')
        verbose_name_plural = _('Tools entries')
