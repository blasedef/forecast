# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Thirdparty

# Create your views here.

def index(request):
	context = {'hello':'Hello world!'}
	return render(request, 'forecast/index.html', context)

def thirdparty(request):
	thirdparty_list = Thirdparty.objects.order_by('name')
	context = {'thirdparty_list': thirdparty_list}
	return render(request, 'forecast/thirdparty/thirdparty.html', context)

def thirdparty_edit(request, thirdparty_id):
	try:
		thirdparty = Thirdparty.objects.get(pk=thirdparty_id)
	except Thirdparty.DoesNotExist:
		raise Http404("Thirdparty does not exist")
	return render(request, 'forecast/thirdparty/thirdparty_edit.html', {'thirdparty': thirdparty })