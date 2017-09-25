# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
# Create your views here.
def index(request):
    context = {
        "courses" : Course.objects.all(),
        "descriptions" : Description.objects.all()
    }
    return render(request, "courses/index.html", context)
def create(request):
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
    else:
        newcourse = Course.objects.create(name=request.POST["name"])
        Description.objects.create(desc=request.POST["desc"], course=newcourse)
    return redirect("/courses")
def destroy(request, id):
    context = {
        "course" : Course.objects.get(id=int(id)),
        "description" : Description.objects.get(course=int(id))
    }
    return render(request, "courses/delete.html", context)
def delete(request, id):
    Course.objects.get(id=int(id)).delete()
    return redirect("/courses")
def show(request, id):
    context = {
        "course" : Course.objects.get(id=int(id)),
        "description" : Description.objects.get(course=int(id)),
        "comments" : Comment.objects.filter(course=int(id))
    }
    return render(request, "courses/comments.html", context)
def createcomment(request, id):
    errors = Comment.objects.validator(request.POST)
    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
    else:
        Comment.objects.create(comment=request.POST["comment"], course=Course.objects.get(id=int(id)))
    return redirect("/courses/"+id+"/comments/show")