from django.shortcuts import render, get_object_or_404, redirect
from toollist.models import Machine, ToolEntry
from toollist.forms import ToolEntryForm


def home(request):
    machines = Machine.objects.all()
    return render(request, 'home.html', locals())

def list_tools(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    entries = ToolEntry.objects.filter(machine=machine).order_by('number')
    return render(request, 'list.html', locals())

def edit(request, pk):
    entry = get_object_or_404(ToolEntry, pk=pk)
    machine = entry.machine
    if request.method == 'POST':
        form = ToolEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('list_tools', entry.machine.pk)
    else:
        form = ToolEntryForm(instance=entry)
    
    return render(request, 'edit.html', locals())

def add(request, machine_pk):
    machine = get_object_or_404(Machine, pk=machine_pk)
    if request.method == 'POST':
        form = ToolEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tools', machine.pk)
    else:
        form = ToolEntryForm(initial={'machine': machine})
    return render(request, 'edit.html', locals())
    
def remove(request, pk):
    entry = get_object_or_404(ToolEntry, pk=pk)
    machine_pk = entry.machine.pk
    entry.delete()
    return redirect('list_tools', machine_pk)
