from django import forms
from django.utils.translation import ugettext as _

from toollist.models import ToolEntry, ToolHolder


class NumberValidationMixin(object):
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['status'] == ToolEntry.MACHINE:
            if not cleaned_data['number']:
                self.add_error('number', _('Number cannot be blank when tool is in machine'))
            else:
                qs = ToolEntry.objects.filter(machine=self.machine, number=cleaned_data['number'])
                if self.instance:
                    qs = qs.exclude(pk=self.instance.pk)
                if qs.exists():
                    self.add_error('number', _('This number is already in use on this machine'))


class ToolEntryForm(NumberValidationMixin, forms.ModelForm):
    def __init__(self, machine, *args, **kwargs):
        super(ToolEntryForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields["holder"].queryset = ToolHolder.objects.filter(machine=machine)
        self.machine = machine

    class Meta:
        model = ToolEntry
        widgets = {'machine': forms.HiddenInput}
        fields = '__all__'


class MillingToolEntryForm(NumberValidationMixin, forms.ModelForm):
    def __init__(self, machine, *args, **kwargs):
        super(MillingToolEntryForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields["holder"].queryset = ToolHolder.objects.filter(machine=machine)
        self.machine = machine

    class Meta:
        model = ToolEntry
        widgets = {'machine': forms.HiddenInput}
        exclude = ('name', 'geometry_x', 'geometry_z', 'geometry_r', 'geometry_y', 'geometry_c', 'wear_x', 'wear_z',
                   'wear_r', 'wear_y', 'wear_c',)
