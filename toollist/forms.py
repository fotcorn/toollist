from django import forms
from smart_selects.widgets import ChainedSelect

from toollist.models import ToolEntry

class ToolEntryForm(forms.ModelForm):
    class Meta:
        model = ToolEntry
        #widgets = {'tool': ChainedSelect}