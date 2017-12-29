# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Teamlist(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    phone_regex = RegexValidator(regex=r'^\d{10,12}$', message="Phone number must be entered in the format: '9999999999'. Up to 12 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=12, blank=False)
    email = models.EmailField(unique=True, blank=False)
    role = models.BooleanField(default=0, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
