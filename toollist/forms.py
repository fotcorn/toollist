from django import forms

from toollist.models import ToolEntry, ToolHolder

class ToolEntryForm(forms.ModelForm):
    
    def __init__(self, machine, *args, **kwargs):
        super(ToolEntryForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        self.fields["holder"].queryset = ToolHolder.objects.filter(machine=machine)
    
    class Meta:
        model = ToolEntry
        widgets = {'machine': forms.HiddenInput}