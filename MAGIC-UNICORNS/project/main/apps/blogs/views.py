from django.shortcuts import render, HttpResponse, redirect
from .models import Blog
from django.core.urlresolvers import reverse

def index(request):
	context = {
		"email" : "blog@gmail.com",
		"name" : "mike"
	}
	return render(request, "blogs/index.html", context)

def update(request):
	errors = Blog.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems(): messages.error(request, error, extra_tags=tag)
		return redirect('/blog/edit/'+id)
	else:
		blog = Blog.objects.get(id = id)
		blog.name = request.POST['name']
		blog.desc = request.POST['desc']
		blog.save()
		return redirect('/blogs')

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
	if request.method == "POST":
		print "*"*50
		print request.POST
		print request.POST['name']
		print request.POST['desc']
		request.session['name'] = request.POST['name']
		request.session['counter'] = 100
		print "*"*50
		return redirect("/blogs")
	else:
		return redirect("/blogs")

def show(request, blog_id):
    print blog_id
    return HttpResponse("placeholder to display blog {}".format(blog_id))

def edit(request, blog_id):
    return HttpResponse("placeholder to edit blog {}".format(blog_id))

def delete(request, blog_id):
    return redirect('/blogs')
