from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    return render(request, 'home/index.html')


def desktop(request):
    return HttpResponse('<div id="desktop-background"></div>')


def chrome_app(request):
    # Make query here
    context = {
        'programName': 'Google Chrome',
        'programId': 'chrome',
    }
    rendered = render_to_string('home/apps/chrome.html', context)
    return HttpResponse(rendered)


