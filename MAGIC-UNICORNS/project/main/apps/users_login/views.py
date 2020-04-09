from django.shortcuts import render, HttpResponse, redirect
from .models import Blog

from models import *

def index(request):
	return HttpResponse("This is where the users will be displayed")
