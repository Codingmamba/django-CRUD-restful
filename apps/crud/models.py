# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print "This is from the form: ", request.POST['full_name']
        if len(postData['full_name']) < 1:
            errors["full_name"] = "Please enter in Your full name"
        if len(postData['email']) < 3:
            errors["email"] = "Please enter in a email address"
        return errors


class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.full_name
