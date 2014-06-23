#!/usr/bin/python
#import tornado
from servicelog.models import ServiceList
import subprocess
import os
from tornado.websocket import WebSocketHandler
#import webtail.webtail
'''
Author: Reza Bakhshayeshi
Email: reza.b2008@gmail.com
Version: 0.1
Tailing a log file and returning the output.
'''


def servicelog(log_name, *args):
    obj = ServiceList.objects.filter(log_name=log_name)
    obj_path = obj[0].log_path
    f1 = open(obj_path)
    for line, l in enumerate(f1):
        pass
    line += 1
    size = os.path.getsize(obj_path)
    if args:
        cmd1 = "tail" + " -" + str(args[-1]) + " " + obj_path
    else:
        cmd1 = "tail " + obj_path
    p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)
    output = p1.communicate()[0]
    return output, line, size