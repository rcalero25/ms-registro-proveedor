# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class usuarios(models.Model):
	nombre = models.CharField(max_length=10)
	apellido = models.CharField(max_length=10)
	correo = models.CharField(max_length=200)
	contrasena = models.CharField(max_length=10)

	def _str_(self):
		return self.nombre



