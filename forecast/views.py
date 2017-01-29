# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import ThirdParty
from .forms import ThirdPartyForm

# Create your views here.
def thirdPartyList(request):
	thirdPartyList = ThirdParty.objects.all()

	if request.method == 'GET':
		thirdPartyForm = ThirdPartyForm()
	else:
		thirdPartyForm = ThirdPartyForm(data=request.POST)
		if thirdPartyForm.is_valid():
			thirdParty = thirdPartyForm.save(commit=False)
			thirdParty.save()

	context = {\
				'thirdPartyList': thirdPartyList,\
				'thirdPartyForm': thirdPartyForm,\
				}\

	return render(request, 'forecast/third_party/third_party_list.html', context)


def thirdPartyEdit(request, thirdParty_id=None):

	html = 'forecast/third_party/third_party_edit.html'
	title = "Edit"
	thirdParty = get_object_or_404(ThirdParty, id=thirdParty_id)
	method = request.method	

	if method == 'GET':
		thirdPartyForm = ThirdPartyForm(instance=thirdParty)
		context = {'title': title, 'thirdPartyForm': thirdPartyForm}
		return render(request,html,context)

	else:
		data=request.POST
		thirdPartyForm = ThirdPartyForm(data=data, instance=thirdParty)
		thirdParty_id = thirdParty.id

		if 'delete' in data:
			thirdParty.delete()
			return redirect('/forecast/third_party/list/')
		else:
			if thirdPartyForm.is_valid():
				thirdParty = thirdPartyForm.save(commit=False)
				if 'save' in data:
					thirdParty.save()
					return redirect('/forecast/third_party/list/')	

def thirdPartyNew(request):

	html = 'forecast/third_party/third_party_new.html'
	title = "New"
	method = request.method	

	if method == 'GET':
		thirdPartyForm = ThirdPartyForm()
		context = {'title': title, 'thirdPartyForm': thirdPartyForm}
		return render(request,html,context)

	else:
		data=request.POST
		thirdPartyForm = ThirdPartyForm(data=data)
		if thirdPartyForm.is_valid():
			if 'save' in data:
				thirdParty = thirdPartyForm.save(commit=False)
				thirdParty.save()
				return redirect('/forecast/third_party/list/')	