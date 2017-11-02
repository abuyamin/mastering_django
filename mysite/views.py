from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def hello(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse("Hello there!</br>Welcome to %s</br>Your browser is %s"
                        %(request.path, ua))

def display_meta(request):
    keys = request.META.keys()
    keys = list(keys)
    keys.sort()
    html = []
    for k in keys:
        v = request.META.get(k, None)
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['subject'], cd['message'],
                      cd.get('email', 'noreply@example.com'),
                      ['siteowner@example.com'],
                      )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'ch-6/custom_contact.html', {'form': form})
