# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import usuarios
from . serializers import usuarioSerializer

#proveedores
from django.contrib.auth.forms import UserCreationForm

def home(request):
	return render(request, 'webapp/login.html')

def registroProveedor(request):
	global args
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('webapp/home.html')
	else:
		form = UserCreationForm()
		args = {'form': form}
	return render(request, 'webapp/registro_formu.html', args)

class listaUsuarios(APIView):

	def get(self, request):
		usuario1 = usuarios.objects.all()
		serializer= usuarioSerializer(usuario1, many=True)

		return Response(serializer.data)


	def post(self):
		pass

