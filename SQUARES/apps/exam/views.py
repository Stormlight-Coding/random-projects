from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, reverse
from django.contrib import messages

def index(request):
    return render(request, "exam/index.html")

def register(request):
	if User.userManager.isValidRegistration(request.POST, request):
		passFlag = True
        return redirect ("/exam")
	passFlag = False
	return redirect("/exam")

def login(request):
    if User.userManager.UserExistsLogin(request.POST, request):
        passFlag = True
        request.session['user_id'] = User.objects.get(username =request.POST['username']).id
        return redirect ('/exam/dashboard')
    else:
        passFlag = False
        return redirect ('/exam')

def dashboard(request):
    context = {
    'user': User.objects.get(id = request.session['user_id']),
    'my_trip': Travel_Plan.objects.filter(users_id = request.session['user_id']),
    'x': (User.objects.get(id = request.session['user_id'])).planned_place.all(),
    'item': Travel_Plan.objects.exclude(users_id = request.session['user_id']),
    }
    return render(request, "exam/dashboard.html", context)

def logout(request):
    del request.session['user_id']
    return redirect ('/exam')

def add(request):
    return render(request, "exam/create.html")

def create(request):
    if Travel_Plan.dateManager.isValidDate(request.POST, request):
        passFlag = True
        Travel_Plan.objects.create(destination = request.POST['destination'],description = request.POST['description'],start = request.POST['start'],end = request.POST['end'],users_id = request.session['user_id'])
        return redirect("/exam/dashboard")
    else:
        passFlag = False
        return redirect("/exam/add")

def include(request, item_id):
    b = Travel_Plan.objects.get(id = item_id)
    print b.destination
    print b.id
    print b.users_id
    x = User.objects.get(id = request.session['user_id'])
    print x
    print x.name
    x.planned_place.add(b)
    return redirect("/exam/dashboard")

def destination(request, item_id):
    b = Travel_Plan.objects.get(id = item_id)
    z = Travel_Plan.objects.get(id = item_id).users_plan.exclude(id = request.session['user_id'])
    context = {
    'place': b,
    'name': z
    }
    return render(request, "exam/destinations.html", context)
