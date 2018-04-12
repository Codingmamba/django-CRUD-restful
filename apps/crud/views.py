from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import *

# Displays the current users in a table and will be able to apply the CRUD method
def index(request):
    context = {
        "users": User.objects.all()
        }
    return render(request, "crud/index.html", context)


# Default route for adding new users and there should be no reason to touch this method
def addUser(request):
    return render(request, "crud/create.html")

# This is the method that is rendering a new user from its form to then becoming redirected
def create(request):
    name = request.POST['full_name']
    email = request.POST['email']
    User.objects.create(full_name=name, email=email)
    return redirect('/')


def show(request, id):
    context = {
        "displays": User.objects.get(id = id)
        }
    return render(request, "crud/show.html", context)


# Update routes
def update(request, id):
    updating_user = User.objects.get(id = id)
    print request.POST['edit_full_name']
    print request.POST['edit_email']
    updating_user.full_name = request.POST['edit_full_name']
    updating_user.email = request.POST['edit_email']
    updating_user.save()
    return redirect('/')


def edit(request, id):
    context = {
        "edits": User.objects.get(id=id)
        }
    return render(request, "crud/edit.html", context)
# Update routes


def delete(request, id):
    User.objects.get(id=id).delete()
    return redirect('/')
