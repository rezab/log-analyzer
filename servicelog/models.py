# Author: Reza Bakhshayeshi
# Email: reza.b2008 [at] gmail [dot] com
# Version: 0.1

from django.db import models


class ServiceList(models.Model):
    log_name = models.CharField(max_length=200)
    log_path = models.CharField(max_length=500)

    def __unicode__(self):
        return self.log_name