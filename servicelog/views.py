# Author: Reza Bakhshayeshi
# Email: reza.b2008 [at] gmail [dot] com
# Version: 0.3

from django.shortcuts import render
from django.http import HttpResponse
from servicelog import servicelist, servicedetail
from servicelog.models import ServiceList


def index(request):
    html = "<html><title>LogAnalyzer Web Service</title><body>The Web Service is Running!</body></html>"
    return HttpResponse(html)


def servicelists(request, *args):
    inc = 10
    logs = ''
    log_name = ''
    global multreq
    if request.POST.get('select', ''):
        multreq = request.POST.getlist('select', '')
        for i in multreq[:-1]:
            logs += servicedetail.multiplelog(i, *args)
            log_name += i + ", "
        else:
            logs += servicedetail.multiplelog(multreq[-1], *args)
            log_name += multreq[-1]
        context = {'logs': logs, 'inc': inc, 'log_name': log_name}
        return render(request, 'multiple.html', context)

    elif request.POST.get('more', ''):
        req = request.POST.get('more')
        inc = int(req) + 10
        for i in multreq[:-1]:
            logs += servicedetail.multiplelog(i, inc)
            log_name += i + ", "
        else:
            logs += servicedetail.multiplelog(multreq[-1], inc)
            log_name += multreq[-1]
        context = {'logs': logs, 'inc': inc, 'log_name': log_name}
        return render(request, 'multiple.html', context)

    elif request.POST.get('less', ''):
        req = request.POST.get('less')
        inc = int(req) - 10
        if inc == 0:
            inc = 10
        for i in multreq[:-1]:
            logs += servicedetail.multiplelog(i, inc)
            log_name += i + ", "
        else:
            logs += servicedetail.multiplelog(multreq[-1], inc)
            log_name += multreq[-1]
        context = {'logs': logs, 'inc': inc, 'log_name': log_name}
        return render(request, 'multiple.html', context)

    elif request.POST.get('refresh', ''):
        inc = request.POST.get('refresh')
        for i in multreq[:-1]:
            logs += servicedetail.multiplelog(i, inc)
            log_name += i + ", "
        else:
            logs += servicedetail.multiplelog(multreq[-1], inc)
            log_name += multreq[-1]
        context = {'logs': logs, 'inc': inc, 'log_name': log_name}
        return render(request, 'multiple.html', context)

    elif request.POST.get('FilterText', ''):
        FilterText = request.POST.get('FilterText')
        filtered, pt_nl = '', ''
        for k in multreq:
            filtered = servicedetail.logpattern(k, FilterText)[0]
            pt_nl = servicedetail.logpattern(k, FilterText)[1]
        for i in multreq[:-1]:
            log_name += i + ", "
        else:
            log_name += multreq[-1]
        context = {'log_name': log_name, 'pt_nl': pt_nl, 'inc': inc, 'filtered': filtered, 'FilterText': FilterText}
        return render(request, 'filterlog2.html', context)

    else:
        instance = servicelist.return_list()
        context = {'instance': instance}
        return render(request, 'index.html', context)


def servicedetails(request, log_name, *args):
    inc = 10
    if request.POST.get('more', ''):
        req = request.POST.get('more')
        inc = int(req) + 10
        logs, nl, size, timestamp = servicedetail.servicelog(log_name, inc)
        if nl < inc:
            inc = int(round(nl, -1))
            logs, nl, size, timestamp = servicedetail.servicelog(log_name, inc)
        context = {'log_name': log_name, 'logs': logs, 'nl': nl, 'inc': inc, 'size': size, 'timestamp': timestamp}
        return render(request, 'log.html', context)

    elif request.POST.get('less', ''):
        req = request.POST.get('less')
        inc = int(req) - 10
        if inc == 0:
            inc = 10
        logs, nl, size, timestamp = servicedetail.servicelog(log_name, inc)
        context = {'log_name': log_name, 'logs': logs, 'nl': nl, 'inc': inc, 'size': size, 'timestamp': timestamp}
        return render(request, 'log.html', context)

    elif request.POST.get('refresh', ''):
        inc = request.POST.get('refresh')
        logs, nl, size, timestamp = servicedetail.servicelog(log_name, inc)
        context = {'log_name': log_name, 'logs': logs, 'nl': nl, 'inc': inc, 'size': size, 'timestamp': timestamp}
        return render(request, 'log.html', context)

    elif request.POST.get('live', ''):
        obj = ServiceList.objects.filter(log_name=log_name)
        obj_path = obj[0].log_path
        context = {'log_name': log_name, 'obj_path': obj_path}
        return render(request, 'livelog.html', context)

    elif request.POST.get('FilterText', ''):
        FilterText = request.POST.get('FilterText')
        filtered, pt_nl = servicedetail.logpattern(log_name, FilterText)
        logs, nl, size, timestamp = servicedetail.servicelog(log_name, inc)
        context = {'log_name': log_name, 'nl': nl, 'pt_nl': pt_nl, 'inc': inc, 'size': size,
                   'timestamp': timestamp, 'filtered': filtered, 'FilterText': FilterText}
        return render(request, 'filterlog.html', context)

    else:
        logs, nl, size, timestamp = servicedetail.servicelog(log_name, *args)
        context = {'log_name': log_name, 'logs': logs, 'nl': nl, 'inc': inc, 'size': size, 'timestamp': timestamp}
        return render(request, 'log.html', context)