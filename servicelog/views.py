from __builtin__ import object
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpRequest
from servicelog import servicelist, servicedetail
'''
Author: Reza Bakhshayeshi
Email: reza.b2008@gmail.com
Version: 0.1
'''

# Create your views here.


def index(request):
    html = "<html><title>LogAnalyzer Web Service</title><body>The Web Service is Running!</body></html>"
    return HttpResponse(html)


def servicelists(request):
    instance = servicelist.return_list()
    context = {'instance': instance}
    return render(request, 'index.html', context)


def servicedetails(request, log_name, *args):
    inc = 10
    if request.POST.get('more', ''):
        req = request.POST.get('more')
        inc = int(req) + 10
        logs, nl, size = servicedetail.servicelog(log_name, inc)

    elif request.POST.get('less', ''):
        req = request.POST.get('less')
        inc = int(req) - 10
        if inc == 0:
            inc = 10
        logs, nl, size = servicedetail.servicelog(log_name, inc)

    elif request.POST.get('refresh', ''):
        inc = request.POST.get('refresh')
        logs, nl, size = servicedetail.servicelog(log_name, inc)

    else:
        logs, nl, size = servicedetail.servicelog(log_name, *args)

    context = {'log_name': log_name, 'logs': logs, 'nl': nl, 'inc': inc, 'size': size}
    return render(request, 'log.html', context)