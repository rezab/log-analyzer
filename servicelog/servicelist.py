#!/usr/bin/python
# Author: Reza Bakhshayeshi
# Email: reza.b2008 [at] gmail [dot] com
# Version: 0.1

from servicelog.models import ServiceList


def return_list():
    lists = []
    for field in ServiceList.objects.all():
        lists.append(field)
    return lists