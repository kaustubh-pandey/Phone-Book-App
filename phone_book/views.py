from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render,redirect
from django.template import loader
from django.http import HttpResponse

from django.http import Http404

def kaush(request):
	return render(request,'phonebook/kaush.html')