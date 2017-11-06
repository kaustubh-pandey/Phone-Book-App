# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render,redirect
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.http import Http404
from .forms import *
# Create your views here.
def addNumber(request):
	form1=AddNumber(request.POST or None)
	if request.method=="POST":
		number=request.POST['number']
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		email=request.POST['email']
		if(len(number)!=10):
			return HttpResponse('<h1> Please enter a valid number</h1>')
		p=Phone.objects.filter(pk=number)
		if(len(p)!=0):
			return HttpResponse('<h1> The number already exists</h1>')
		p=Phone(number=number,first_name=first_name,last_name=last_name,email=email)
		p.save()
		return HttpResponse('<h1> Your number has been added</h1>')
	return render(request,'phonebook/add.html',context={'form1':form1})

def search(request):
	form2=Number(request.POST or None)
	context={'form2':form2}
	if request.method=="POST":
		number=request.POST['number']
		print(len(number))
		if(len(number)!=10):
			return HttpResponse('<h1> Please enter a valid number</h1>')
		p=Phone.objects.filter(pk=number)
		if(len(p)==0):
			return HttpResponse('<center><h1> Sorry! The number doesnot exist</h1></center>')
		p=p[0]
		first_name=p.first_name
		last_name=p.last_name
		email=p.email
		return render(request,'phonebook/results.html',context={'number':number,'first_name':first_name,
			'last_name':last_name,'email':email})
	return render(request,'phonebook/search.html',context)

def index(request):
	return render(request,'phonebook/index.html')



