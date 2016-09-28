from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Data(models.Model):
    info = models.CharField(max_length=1000)
