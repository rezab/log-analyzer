from django.db import models
'''
Author: Reza Bakhshayeshi
Email: reza.b2008@gmail.com
Version: 0.1
'''

# Create your models here.


class ServiceList(models.Model):
    log_name = models.CharField(max_length=200)
    log_path = models.CharField(max_length=500)
    def __unicode__(self):
        return self.log_name