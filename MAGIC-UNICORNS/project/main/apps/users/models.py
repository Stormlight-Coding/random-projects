from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "User first name should be more than 2 characters"
        if len(postData['last_name']) < 1:
            errors["desc"] = "User last name should be more than 1 characters"
        if len(postData['email']) < 5:
            errors["desc"] = "User e-mail should be more than 1 characters"
        return errors;

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
