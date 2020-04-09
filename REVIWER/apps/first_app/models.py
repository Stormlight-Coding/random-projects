from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
# import re
#
#
#
# EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def isValidRegistration(self, userInfo, request):
        passFlag = True
        if len(userInfo['name']) < 3:
            messages.warning(request, 'Name is not long enough.')
            passFlag = False
        if len(userInfo['username']) < 3:
            messages.warning(request, 'Username is not long enough.')
            passFlag = False
        if len(userInfo['password']) < 8:
            messages.warning(request, 'Password is not long enough.')
            passFlag = False
        if userInfo['password'] != userInfo['confirm_pw']:
            messages.warning(request, 'Password match not confirmed.')
            passFlag = False
        if User.objects.filter(username = userInfo['username']):
			messages.error(request, "This Username already exists in our database.")
			passFlag = False

        if passFlag == True:
            messages.success(request, "Success! Welcome, " + userInfo['name'] + "!")
            hashed = bcrypt.hashpw(userInfo['password'].encode(), bcrypt.gensalt())
            User.objects.create(name = userInfo['name'], username = userInfo['username'], password = hashed)
        return passFlag
    def UserExistsLogin(self, userInfo, request):
        passFlag = True
        if User.objects.filter(username = userInfo['username']):
            hashed = User.objects.get(username = userInfo['username']).password
            hashed = hashed.encode('utf-8')
            password = userInfo['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                messages.success(request, "Success! Welcome, " + User.objects.get(username = userInfo['username']).name + "!")
                passFlag = True
            else:
                messages.warning(request, "Unsuccessful login. Incorrect password")
                passFlag = False
        else:
            messages.warning(request, "Unsuccessful login. Your Username is incorrect.")
            passFlag = False
        return passFlag

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_hired = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
    objects = models.Manager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    users = models.ForeignKey(User, related_name = "added_book")
    users_book = models.ManyToManyField(User, related_name= "reviewed_book") ####(User.objects.get(id = request.session['user_id'])).wished_item.all() = shows ALL the items that sessions user has clicked on.
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
