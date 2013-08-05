from django import forms
from smart_selects.widgets import ChainedSelect

from toollist.models import ToolEntry

class ToolEntryForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ToolEntryForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = ToolEntry
        widgets = {'machine': forms.HiddenInput}