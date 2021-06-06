from main import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django import forms
from .models import Post
from django.forms import ModelForm, TextInput, FileInput, PasswordInput, widgets


class UserLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'Name', 'placeholder': 'Submit Nickname', 'class': 'formimput', }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'type': 'Password', 'placeholder': 'Submit Password', 'class': 'formimput', }))


class UserRegister(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'Name', 'placeholder': 'Submit Nickname', 'class': 'formimput', }))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'type': 'password', 'placeholder': 'Submit Password', 'class': 'formimput', }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'type': 'password', 'placeholder': 'Submit Password', 'class': 'formimput', }))
    # darkmoe = forms.BooleanField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'type': 'Name', 'placeholder': 'Submit Nickname', 'class': 'formimput', }),
            'email': forms.TextInput(attrs={
                'type': 'Email',
                'placeholder': 'Submit Email',
                'class': 'formimput',
            }),
            'password1': forms.PasswordInput(attrs={
                'type': 'password',
                'placeholder': 'Submit Password',
                'class': 'formimput',
            }),
            'password2': forms.PasswordInput(attrs={
                'type': 'password',
                'placeholder': 'Confirm Password',
                'class': 'password',
            }),
        }


class ImageForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'heading',
            'instagram',
            'image',
            'authors_id',
            'type',
        ]


class VideoForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'heading',
            'instagram',
            'url',
            'authors_id',
            'type',
        ]


# class AddPost(ModelForm):
#     class Meta:s
#         model = Post
#         fields = ('heading', 'instagram', 'image', 'author')
#         widgets = {
#             'heading': forms.TextInput(attrs={
#                 'type': 'heading',
#                 'placeholder': 'Heading, max 150 characters',
#                 'class': 'formimput',
#             }),
#             'instagram': forms.TextInput(attrs={'type': 'nikname','placeholder': 'Your Instagram','class': 'formimput',}),
#         }


# class UserReg(forms.Form):
#     name = forms.CharField(max_length=150, label='Name')
#     email = forms.CharField(max_length=150, label='Email')
#     password = forms.CharField(max_length=100, label='Password')
#     ava = forms.ImageField(label='Image',required=True)


#     class Meta:
#         model = User
#         fields = ['name', 'email', 'password', 'instagram', 'age', 'ava']

#         widgets = {
#             'name': TextInput(attrs={
#                 'type':'Name',
#                 'placeholder':'Submit Name',
#                 'class':'formimput',
#             }),
#             'email': TextInput(attrs={
#                 'type':'Email',
#                 'placeholder':'Submit Email',
#                 'class':'formimput',
#             }),
#             'password': PasswordInput(attrs={
#                 'type':'Password',
#                 'placeholder':'Submit Passord',
#                 'class':'formimput',
#             }),
#             'instagram': TextInput(attrs={
#                 'type':'Name',
#                 'placeholder':'@YourInstagram',
#                 'class':'formimput',
#             }),
#             'ava': FileInput(attrs={
#                 'type':'File',
#                 'class':'formimputfile',
#             }),
#         }
