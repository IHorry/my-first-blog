from django.conf import settings
from django.db import models
from django import forms
from django.utils import timezone
import os

class Skill(models.Model):
    skill = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Qual(models.Model):
    qualification = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    coverImage = models.ImageField(upload_to='images/',default="/images/default.jpg")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class CV(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    summary = models.TextField()
    interests = models.TextField()
    references = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title




class Work(models.Model):
    title = models.TextField(max_length=200)
    company = models.TextField()
    dateStarted = models.DateField(blank=True, null=True)
    dateEnd = models.DateField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

