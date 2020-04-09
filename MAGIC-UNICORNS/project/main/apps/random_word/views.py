from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	return render(request,'random_word/index.html')

def generate(request):
	if 'counter'in request.session:
		request.session['counter'] += 1
	else:
		request.session['counter'] = 1
	context = {
    	"word" : get_random_string(length = 14),
		"attempt" : request.session['counter']
		}
	print request.session['counter']
	return render(request,'random_word/index.html', context)

def reset(request):
	request.session['counter'] = 0
	return redirect("/random_word")