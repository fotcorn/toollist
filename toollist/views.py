from django.shortcuts import render, get_object_or_404, redirect
from toollist.models import Machine, ToolEntry
from toollist.forms import ToolEntryForm, MillingToolEntryForm


def home(request):
    machines = Machine.objects.all()
    return render(request, 'home.html', locals())


def list_tools(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    entries = ToolEntry.objects.filter(machine=machine).select_related('tool', 'type', 'holder', 'cooling')

    if request.GET.get('sort') == 'type':
        entries = entries.order_by('status', 'type__name', 'tool__name')
    elif request.GET.get('sort') == 'holder':
        entries = entries.order_by('status', 'holder', 'pliers')
    elif request.GET.get('sort') == 'name':
        entries = entries.order_by('status', 'name', 'number')
    else:
        entries = entries.order_by('status', 'number')
    return render(request, 'list.html', locals())


def edit_milling(request, pk):
    entry = get_object_or_404(ToolEntry, pk=pk)
    machine = entry.machine
    if request.method == 'POST':
        form = MillingToolEntryForm(machine, request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('list_tools', entry.machine.pk)
    else:
        form = MillingToolEntryForm(machine, instance=entry)

    return render(request, 'edit.html', locals())


def add_milling(request, machine_pk):
    machine = get_object_or_404(Machine, pk=machine_pk)
    if request.method == 'POST':
        form = MillingToolEntryForm(machine, request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tools', machine.pk)
    else:
        form = MillingToolEntryForm(machine, initial={'machine': machine})
    return render(request, 'edit.html', locals())


def edit_turning(request, pk):
    entry = get_object_or_404(ToolEntry, pk=pk)
    machine = entry.machine
    if request.method == 'POST':
        form = ToolEntryForm(machine, request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('list_tools', entry.machine.pk)
    else:
        form = ToolEntryForm(machine, instance=entry)

    return render(request, 'edit.html', locals())


def add_turning(request, machine_pk):
    machine = get_object_or_404(Machine, pk=machine_pk)
    if request.method == 'POST':
        form = ToolEntryForm(machine, request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tools', machine.pk)
    else:
        form = ToolEntryForm(machine, initial={'machine': machine})
    return render(request, 'edit.html', locals())


def remove(request, pk):
    entry = get_object_or_404(ToolEntry, pk=pk)
    machine_pk = entry.machine.pk
    entry.delete()
    return redirect('list_tools', machine_pk)
