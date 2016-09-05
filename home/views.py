from ast import literal_eval
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from home.models import (App, ProcessList, MemorySpace, MemoryTable)
from django.db import IntegrityError
from django.db.models import Sum
from home.disk import fifo, scan, cscan
from random import randint


def index(request):
    ProcessList.objects.all().delete()
    MemorySpace.objects.all().delete()
    MemoryTable.objects.all().delete()

    l = [1] * 10 + [0] * 54

    MemorySpace(app=App.objects.get(app_id="system"), start=0, length=10).save()
    MemoryTable(name="Ram", list=str(l), list_length=64).save()
    MemoryTable(name="Swap", list=str([0] * 64), list_length=64).save()

    apps = App.objects.all().exclude(app_id='system')

    return render(request, 'home/index.html', {'apps': apps})


def show_desktop(request):
    rendered = render_to_string('home/windows/desktop.html')
    return HttpResponse(rendered)


def open_app(request, app_id):
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

    total_memory = MemoryTable.objects.get(name="Ram").list_length

    context = {
        'cpu_use': cpu_use,
        'memory_use': memory_use,
        'disk_use': disk_use,
        'total_memory': total_memory,
        'p_memory_use': (memory_use * 100) / total_memory
    }

    rendered = render_to_string('home/reports/resources.html', context)
    return HttpResponse(rendered)


def show_memory_table(request):
    context = {
        'list': literal_eval(MemoryTable.objects.get(name="Ram").list)
    }

    rendered = render_to_string('home/reports/memory_table.html', context)
    return HttpResponse(rendered)


def add_to_memory_table(request, app_id):
    app = App.objects.get(app_id=app_id)
    memory = app.memory_use
    memory_table = MemoryTable.objects.get(name="Ram")
    l = literal_eval(memory_table.list)
    first = True
    count = 0
    start = 0
    c = ProcessList.objects.filter(app=app).count()

    if c == 0:
        for i in range(len(l)):
            if memory > 0:
                if l[i] == 0:
                    if first:
                        start = i
                        first = False
                    l[i] = app.id
                    count += 1
                    memory -= 1
                if i < len(l) - 1 and count > 0:
                    if l[i + 1] != 0:
                        MemorySpace(app=app, start=start, length=count).save()
                        first = True
                        count = 0
                if i == len(l) - 1 and count > 0:
                    MemorySpace(app=app, start=start, length=count).save()
                    first = True
                    count = 0
            else:
                MemorySpace(app=app, start=start, length=count).save()
                break

        memory_table.list = str(l)
        memory_table.save()

    context = {
        'list': l
    }

    rendered = render_to_string('home/reports/memory_table.html', context)
    return HttpResponse(rendered)


def remove_from_memory_table(request, app_id):
    app = App.objects.get(app_id=app_id)
    memory_table = MemoryTable.objects.get(name="Ram")
    l = literal_eval(memory_table.list)

    for i in range(len(l)):
        if l[i] == app.id:
            l[i] = 0

    memory_table.list = str(l)
    memory_table.save()

    MemorySpace.objects.filter(app=app).delete()

    context = {
        'list': l
    }

    rendered = render_to_string('home/reports/memory_table.html', context)
    return HttpResponse(rendered)


def compact_memory_table(request):
    memory_table = MemoryTable.objects.get(name="Ram")
    pages = MemorySpace.objects.all().exclude(app__app_id='system').order_by('app')
    pages_count = len(pages) - 1

    l = ([1] * 10 + [0] * 54)
    p = 0
    i = 10

    while i < len(l):
        start = i
        for j in range(pages[p].length):
            l[i] = pages[p].app.id
            i += 1

        MemorySpace(app=pages[p].app, start=start, length=pages[p].length).save()
        pages[p].delete()

        if p < pages_count:
            p += 1
        else:
            break

    memory_table.list = str(l)
    memory_table.save()

    context = {
        'list': l
    }

    rendered = render_to_string('home/reports/memory_table.html', context)
    return HttpResponse(rendered)


def change_process_state(request, app_id):
    if app_id != "system":
        process = ProcessList.objects.get(app__app_id=app_id)
        process.status = not process.status
        process.save()

    context = {
        'processes_list': ProcessList.objects.all()
    }

    rendered = render_to_string('home/reports/processes_table.html', context)
    return HttpResponse(rendered)


def get_memory_available(request):
    processes = ProcessList.objects.all().aggregate(Sum('app__memory_use'))
    return HttpResponse(64 - int(processes.get('app__memory_use__sum')))


def get_memory_app(request, app_id):
    app = App.objects.get(app_id=app_id)
    return HttpResponse(app.memory_use)


def get_all_open_apps(request):
    processes = ProcessList.objects.all()
    apps = str()
    for process in processes:
        apps += str(process.app.app_id) + " "

    return HttpResponse(apps)


def get_disabled_processes(request):
    print(ProcessList.objects.filter(status=False).count())
    return HttpResponse(ProcessList.objects.filter(status=False).count())


def show_swap_table(request):
    context = {
        'list': literal_eval(MemoryTable.objects.get(name="Swap").list)
    }

    rendered = render_to_string('home/reports/memory_table.html', context)
    return HttpResponse(rendered)


def swap_out(request, app_id):
    disabled_processes = ProcessList.objects.filter(status=False)
    app = App.objects.get(app_id=app_id)
    memory = app.memory_use
    needed_memory = app.memory_use - (64 - int(ProcessList.objects.all().aggregate(Sum('app__memory_use')).get(
        'app__memory_use__sum')))

    swap_table = MemoryTable.objects.get(name="Swap")
    swap_list = literal_eval(swap_table.list)

    ram_table = MemoryTable.objects.get(name="Ram")
    ram_list = literal_eval(ram_table.list)

    apps_to_swap_out = set()

    for process in disabled_processes:
        if needed_memory > 0:
            needed_memory -= process.app.memory_use
            apps_to_swap_out.add(process.app.id)

    i = 0
    while i < len(swap_list):
        for p in apps_to_swap_out:
            for j in range(App.objects.get(id=p).memory_use):
                if swap_list[i] == 0:
                    swap_list[i] = p
                i += 1
            MemorySpace.objects.filter(app=p).delete()
        break

    # for i in range(len(swap_list)):
    #     if memory > 0:
    #         if swap_list[i] == 0:
    #             swap_list[i] = app.id
    #             memory -= 1
    #     else:
    #         break

    swap_table.list = swap_list
    swap_table.save()

    for i in range(len(ram_list)):
        if ram_list[i] in apps_to_swap_out:
            ram_list[i] = 0

    ram_table.list = ram_list
    ram_table.save()

    # ProcessList.objects.filter(app=app).delete()

    """
    def compact_memory_table(request):
        memory_table = MemoryTable.objects.get(name="Ram")
        pages = MemorySpace.objects.all().exclude(app__app_id='system').order_by('app')
        pages_count = len(pages) - 1

        l = ([1] * 10 + [0] * 22)
        p = 0
        i = 10

        while i < len(l):
            start = i
            for j in range(pages[p].length):
                l[i] = pages[p].app.id
                i += 1

            MemorySpace(app=pages[p].app, start=start, length=pages[p].length).save()
            pages[p].delete()

            if p < pages_count:
                p += 1
            else:
                break

        memory_table.list = str(l)
        memory_table.save()

        context = {
            'list': l
        }

    def add_to_memory_table(request, app_id):
        app = App.objects.get(app_id=app_id)
        memory = app.memory_use
        memory_table = MemoryTable.objects.get(name="Ram")
        l = literal_eval(memory_table.list)
        first = True
        count = 0
        start = 0
        c = ProcessList.objects.filter(app=app).count()

        if c == 0:
            for i in range(len(l)):
                if memory > 0:
                    if l[i] == 0:
                        if first:
                            start = i
                            first = False
                        l[i] = app.id
                        count += 1
                        memory -= 1
                    if i < len(l) - 1 and count > 0:
                        if l[i + 1] != 0:
                            MemorySpace(app=app, start=start, length=count).save()
                            first = True
                            count = 0
                    if i == len(l) - 1 and count > 0:
                        MemorySpace(app=app, start=start, length=count).save()
                        first = True
                        count = 0
                else:
                    MemorySpace(app=app, start=start, length=count).save()
                    break

            memory_table.list = str(l)
            memory_table.save()
    """

    context = {
        'list': swap_list
    }

    rendered = render_to_string('home/reports/memory_table.html', context)
    return HttpResponse(rendered)


def swap_in(request, app_id):
    pages = MemorySpace.objects.filter(app__processlist__status=False)
    for page in pages:
        print(page.app.app_id)

    return HttpResponse(str(pages))


def get_disk_positions(request):
    processes = ProcessList.objects.all().reverse()

    disk_pos = list()

    for process in processes:
        disk_pos.append(process.app.disk_position)

    context = {
        'v': disk_pos
    }

    rendered = render_to_string('home/reports/disk_vector.html', context)
    return HttpResponse(rendered)


def apply_fifo(request):
    processes = ProcessList.objects.all().reverse()

    disk_pos = list()
    i = randint(0, 200)

    for process in processes:
        disk_pos.append(process.app.disk_position)

    v, a = fifo(disk_pos, i)

    context = {
        'v': v,
        'start': i
    }

    rendered = render_to_string('home/reports/disk_vector.html', context)
    return HttpResponse(rendered)


def apply_scan(request):
    processes = ProcessList.objects.all().reverse()

    disk_pos = list()
    i = randint(0, 200)

    for process in processes:
        disk_pos.append(process.app.disk_position)

    v, a = scan(disk_pos, i)

    context = {
        'v': v,
        'start': i
    }

    rendered = render_to_string('home/reports/disk_vector.html', context)
    return HttpResponse(rendered)


def apply_cscan(request):
    processes = ProcessList.objects.all().reverse()

    disk_pos = list()
    i = randint(0, 200)

    for process in processes:
        disk_pos.append(process.app.disk_position)

    v, a = cscan(disk_pos, i)

    context = {
        'v': v,
        'start': i
    }

    rendered = render_to_string('home/reports/disk_vector.html', context)
    return HttpResponse(rendered)

"""
disco:
    Asociar pos de discos a cada app
    Generar un vector con las apps abiertas con cada pos de disco
    Aplicar los algoirimos a ese vector
    Mostrar vector resultante


"""