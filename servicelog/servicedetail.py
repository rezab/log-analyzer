#!/usr/bin/env python
# Author: Reza Bakhshayeshi
# Email: reza.b2008 [at] gmail [dot] com
# Version: 0.2

from servicelog.models import ServiceList
import subprocess
import os
import time


def servicelog(log_name, *args):
    obj = ServiceList.objects.filter(log_name=log_name)
    obj_path = obj[0].log_path
    try:
        f1 = open(obj_path)
    except:
        raise IOError
    for line, l in enumerate(f1):
        pass
    size = os.path.getsize(obj_path)
    if size > 0:
        line += 1
    else:
        line = 0
    timestamp = os.path.getmtime(obj_path)
    timestamp = time.ctime(int(timestamp))
    if args:
        cmd1 = "tail" + " -" + str(args[-1]) + " " + obj_path
    else:
        cmd1 = "tail " + obj_path
    p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)
    output = p1.communicate()[0]
    return output, line, size, timestamp


def logpattern(log_name, pattern):
    newpt = ''
    obj = ServiceList.objects.filter(log_name=log_name)
    obj_path = obj[0].log_path
    pattern = pattern.split(',')
    for i, val in enumerate(pattern):
        newpt += " -e " + str(pattern[i])
    cmd1 = "grep " + newpt + " " + obj_path
    p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)
    output = p1.communicate()[0]
    pt_nl = output.count('\n')
    return output, pt_nl


def multiplelog(log_name, *args):
    obj = ServiceList.objects.filter(log_name=log_name)
    obj_path = obj[0].log_path
    if args:
        cmd1 = "tail" + " -" + str(args[-1]) + " " + obj_path
    else:
        cmd1 = "tail " + obj_path
    p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)
    output = p1.communicate()[0]
    return output