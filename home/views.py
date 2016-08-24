from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from home.models import App, ProcessList
from collections import OrderedDict


def index(request):
    # Clear ProcessList
    ProcessList.objects.all().delete()
    return render(request, 'home/index.html')


def show_desktop(request):
    rendered = render_to_string('home/windows/desktop.html')
    return HttpResponse(rendered)


def open_app(request, app_id):
    # Make query here
    app = App.objects.get(app_id=app_id)

    # Add to processes list

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

    ProcessList.objects.create(app=App.objects.get(app_id=app_id))
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
