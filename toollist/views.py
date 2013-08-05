from django.shortcuts import render, get_object_or_404
from toollist.models import Machine, ToolEntry


def home(request):
    machines = Machine.objects.all()
    return render(request, 'home.html', locals())

def list(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    ToolEntry.objects.filter(machine=machine)
    return render(request, 'list.html', locals())
    