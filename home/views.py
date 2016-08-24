from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from home.models import App


def index(request):
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


def close_app(request, app_id):
    # pop app_name from processes list
    return HttpResponse('<div id="desktop-background"></div>')

