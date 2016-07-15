from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    return render(request, 'home/index.html')


def chrome_app(request):
    context = {
        'programName': 'Google Chrome',
        'programId': 'chrome',
    }
    rendered = render_to_string('home/apps/chrome.html', context)
    return HttpResponse(rendered)


