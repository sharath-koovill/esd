from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def geo_locate(request):
	return HttpResponse("your location is here")
