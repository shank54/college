# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sp2011(models.Model):
	Term = models.TextField()
	Subject = models.TextField()
	Catalog = models.TextField()
	Section = models.TextField()
	Title = models.TextField()
	A = models.IntegerField(default=0)
	Aminus = models.IntegerField(default=0)
	Bplus = models.IntegerField(default=0)
	B = models.IntegerField(default=0)
	Bminus = models.IntegerField(default=0)
	Cplus = models.IntegerField(default=0)
	C = models.IntegerField(default=0)
	P = models.IntegerField(default=0)
	S = models.IntegerField(default=0)
	D = models.IntegerField(default=0)
	F = models.IntegerField(default=0)
	U = models.IntegerField(default=0)
	I = models.IntegerField(default=0)
	IP = models.IntegerField(default=0)
	W = models.IntegerField(default=0)
	Total_Grades = models.IntegerField(default=0)
	Avg_Grade_in_Grade_Points = models.FloatField(default=0)
	Primary_Instructor = models.TextField()
