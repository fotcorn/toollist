from django.shortcuts import render, get_object_or_404, redirect
from toollist.models import Machine, ToolEntry
from toollist.forms import ToolEntryForm


def home(request):
    machines = Machine.objects.all()
    return render(request, 'home.html', locals())

def list(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    entries = ToolEntry.objects.filter(machine=machine).order_by('number')
    return render(request, 'list.html', locals())

def edit(request, pk):
    entry = get_object_or_404(ToolEntry, pk=pk)
    
    if request.method == 'POST':
        form = ToolEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('list', entry.machine.pk)
    else:
        form = ToolEntryForm(instance=entry)
    
    return render(request, 'edit.html', locals())
    