from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, reverse
from django.contrib import messages

def index(request):
    return render(request, "first_app/index.html")

def register(request):
	if User.userManager.isValidRegistration(request.POST, request):
		passFlag = True
        return redirect ("/first_app")
	passFlag = False
	return redirect("/first_app")

def login(request):
    if User.userManager.UserExistsLogin(request.POST, request):
        passFlag = True
        request.session['user_id'] = User.objects.get(username =request.POST['username']).id
        # request.session['user_id'] = result.id
        return redirect ('/first_app/dashboard')
    else:
        passFlag = False
        return redirect ('/first_app')

def dashboard(request):
    x = (User.objects.get(id = request.session['user_id'])).reviewed_book.all()
    print x
    context = {
    'user': User.objects.get(id = request.session['user_id']),
    'book': Book.objects.exclude(users_id = request.session['user_id']),
    'x': (User.objects.get(id = request.session['user_id'])).reviewed_book.all(),
    # 'z': (User.objects.exclude(id = request.session['user_id'])).reviewed_book.all()
    # 'my_item': Item.objects.filter(users_id = request.session['user_id']),
    # 'item': Item.objects.exclude(users_id = request.session['user_id']),
    # 'x': (User.objects.get(id = request.session['user_id'])).wished_item.all()
    }
    return render(request, "first_app/dashboard.html", context)

def logout(request):
    del request.session['user_id']
    return redirect ('/first_app')

def add(request):
    x =  Book.objects.all()
    print x
    context = {
    'author' : x,
    }
    return render(request, "first_app/add.html", context)

def create(request):
    if request.method == 'POST':
        Book.objects.create(title = request.POST['title'],author = request.POST['author'], review = request.POST['review'], rating = request.POST['rating'], users_id = request.session['user_id'])
        x = Book.objects.get(title = request.POST['title'])
        b = User.objects.get(id = request.session['user_id'])
        x.users_book.add(b)
        return redirect("/first_app/dashboard")

def book_info(request, book_id):
    b = Book.objects.get(id = book_id)
    print b.title
    z = (Book.objects.get(id = book_id)).users_book.all()
    print z
    context = {
    'book': b,
    'name': z,
    }
    return render(request, "first_app/book.html", context)

def add_review(request, book_id):
    if request.method == 'POST':
        # Book.objects.create(title = request.POST['title'],author = request.POST['author'], review = request.POST['review'], rating = request.POST['rating'], users_id = request.session['user_id'])
        x = Book.objects.get(id = book_id)
        print x.title
        b = User.objects.get(id = request.session['user_id'])
        # x.users_book.add(b)
        return redirect("/first_app/dashboard")
