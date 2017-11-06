# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Phone(models.Model):
	number=models.CharField(max_length=10,primary_key=True)
	first_name=models.CharField(max_length=10)
	last_name=models.CharField(max_length=10)
	email=models.CharField(max_length=20)

	def __str__(self):
		return self.number