from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# class Usernononon(models.Model):
#     name = models.CharField('Name',max_length=150)
#     email = models.EmailField('Email')
#     password = models.CharField('Password',max_length=150)
#     instagram = models.CharField('Instagram',max_length=150,blank=True)
#     darkmoe = models.BooleanField(default=False,auto_created=True)
#     age = models.DateField('Age')
#     registrationdate = models.DateTimeField('Registration Date',auto_now=True)
#     ava = models.FileField('img',blank=True)


def aresSilka(url):
    if 'youtube.com/' not in url:
        return ValidationError('You can only put YouTube videos')
    elif 'https://youtu.be/' not in url:
        return ValidationError('You can only put YouTube videos')


class Post(models.Model):

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, related_name='ImageAuthor')
    heading = models.TextField('Heading', max_length=753)
    instagram = models.CharField('Instagram', max_length=150, blank=True)
    PostingDate = models.DateTimeField('Registration Date', auto_now=True)
    type = models.CharField(max_length=5, blank=True, default='img')
    image = models.ImageField(max_length=150)
    url = models.URLField(null=True,max_length=150, validators=[aresSilka])
    authors_id = models.IntegerField(default=1, blank=True)
    

    def __str__(self):
        return self.heading

