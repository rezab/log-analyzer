#!/usr/bin/python
from servicelog.models import ServiceList
'''
Author: Reza Bakhshayeshi
Email: reza.b2008@gmail.com
Version: 0.1
Listing corresponding services of log files.
'''

def return_list():
    lists = []
    for field in ServiceList.objects.all():
        lists.append(field)
    return lists