from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
	context = {
		"name" : User.objects.all()
	}
	return render(request, "users/index.html", context)

def create(request):
	if request.method == 'POST':
		User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
		return redirect("/users")
	else:
		return redirect("/users")

def new(request):
    return render(request, "users/new.html")

def show(request, user_id):
	print user_id
	context = {
		'id' : User.objects.get(id = user_id)
		}
	return render(request, "users/show.html", context)

def edit(request, user_id):
	print user_id
	context = {
		'id' : User.objects.get(id = user_id)
		}
	return render(request,'users/edit.html', context)

def change(request, user_id):
	print user_id
	if request.method == 'POST':
		print "HASJDHASHFOHWQORFHKJDF"
		b = User.objects.get(id = user_id)
		if request.POST['first_name'] > 0 and request.POST['last_name'] > 0 and request.POST['email'] > 0:
			b.first_name = request.POST['first_name']
			b.last_name = request.POST['last_name']
			b. email = request.POST['email']
			b.save()
			return redirect('/users')
		else:
			return redirect('users')
	else:
		return redirect('/users')


def delete(request, user_id):
	b = User.objects.get(id = user_id)
	b.delete()
	print user_id
	return redirect('/users')

# def update(request):
#     errors = User.objects.basic_validator(request.POST)
# 		if len(errors):
# 			for tag, error in errors.iteritems(): messages.error(request, error, extra_tags=tag)
# 			return redirect('/user/edit/'+id)
# 		else:
# 			user = User.objects.get(id = id)
# 			user.first_name = request.POST['first_name']
# 			user.last_name = request.POST['last_name']
# 			user.email = request.POST['email']
# 			user.save()
# # 			return redirect('/users')
#
