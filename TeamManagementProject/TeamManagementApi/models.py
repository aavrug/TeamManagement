# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teamlist(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=12, blank=False)
    email = models.EmailField(unique=True, blank=False)
    role = models.BooleanField(default=0, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
