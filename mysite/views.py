from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render
import datetime


def hello(request):
    return HttpResponse("Hello there!")


def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render(request, 'ch-2/current_datetime.html',
                  {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'ch-2/hours_ahead.html',
                  {'hour_offset': offset, 'next_time': dt})
