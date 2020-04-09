from django.shortcuts import render, HttpResponse, redirect
from .models import Course

def index(request):
	context = {
		"name" : Course.objects.all()
	}
	return render(request, "course/index.html", context)

def create(request):
	if request.method == 'POST':
		Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
		return redirect("/course")
	else:
		return redirect("/course")

def destroy(request, course_id):
    context = {'id' : Course.objects.get(id = course_id)}
    return render(request, "course/delete.html", context)

def delete(request, course_id):
	b = Course.objects.get(id = course_id)
	b.delete()
	return redirect('/course')
