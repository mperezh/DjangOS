from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from home.models import App, ProcessList, MemorySpace, MemoryTable
from django.db import IntegrityError
# from collections import OrderedDict


def index(request):
    # Clear ProcessList
    ProcessList.objects.all().delete()
    MemorySpace.objects.all().delete()
    MemoryTable.objects.all().delete()

    l = [1,1,1,1,1] + ([0] * 1019)
    m = MemoryTable(list=str(l), list_length=1024)
    m.save()

    return render(request, 'home/index.html')


def show_desktop(request):
    rendered = render_to_string('home/windows/desktop.html')
    return HttpResponse(rendered)


def open_app(request, app_id):
    # Make query here
    app = App.objects.get(app_id=app_id)

    context = {
        'app_id': app.app_id,
        'app_name': app.app_name,
    }
    rendered = render_to_string('home/windows/app.html', context)
    return HttpResponse(rendered)


def close_app(request):
    rendered = render_to_string('home/windows/desktop.html')
    return HttpResponse(rendered)


def add_process(request, app_id):
    try:
        ProcessList.objects.create(app=App.objects.get(app_id=app_id))
    except IntegrityError as e:
        print("Exception:", e.__cause__, "(App already on process list)")

    context = {
        'processes_list': ProcessList.objects.all()
    }

    rendered = render_to_string('home/reports/processes_table.html', context)
    return HttpResponse(rendered)


def remove_process(request, app_id):
    ProcessList.objects.filter(app=App.objects.get(app_id=app_id)).delete()

    context = {
        'processes_list': ProcessList.objects.all()
    }

    rendered = render_to_string('home/reports/processes_table.html', context)
    return HttpResponse(rendered)


def resources(request):
    cpu_use = 0
    memory_use = 0 
    disk_use = 0 

    for process in ProcessList.objects.all():
        cpu_use += process.app.cpu_use
        memory_use += process.app.memory_use
        disk_use += process.app.disk_use

    context = {
        'cpu_use': cpu_use,
        'memory_use': memory_use,
        'disk_use': disk_use
    }

    rendered = render_to_string('home/reports/resources.html', context)
    return HttpResponse(rendered)


def add_to_memory_table(request, app_id):
    pass
