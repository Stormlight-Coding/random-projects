from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

def index(request):
	return render(request, 'surveys/index.html')

def results(request):
	context = {
		"name": request.session['name'],
		"location": request.session['location'],
		"language": request.session['language'],
		"desc": request.session['desc'],
	}
	return render(request, 'surveys/results.html', context)

def process(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['desc'] = request.POST['desc']
	return redirect('/surveys/results')

