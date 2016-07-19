from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    return render(request, 'home/index.html')


def desktop(request):
    return HttpResponse('<div id="desktop-background"></div>')


def open_app(request, app_name):
    # Make query here
    context = {
        'programName': 'Google Chrome',
        'programId': app_name,
    }
    rendered = render_to_string('home/apps/{0}.html'.format(app_name), context)
    return HttpResponse(rendered)


