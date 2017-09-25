# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["name"])<=5:
            errors["name"]= "Course name must be more than 5 characters"
        if len(postData["desc"])<=15:
            errors["desc"]= "Course description must be more than 15 characters"
        return errors
class CommentManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["comment"])<=1:
            errors["comment"]= "Comment cannot be blank"
        return errors
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
class Description(models.Model):
    desc = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    course = models.OneToOneField(Course, related_name="description", on_delete=models.CASCADE)
class Comment(models.Model):
    comment = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    objects = CommentManager()