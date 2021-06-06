from os import error
from typing import List
from django.contrib import auth
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .forms import UserLogin, UserRegister , VideoForm , ImageForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login as auth_login, logout as logoutuser, models
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
# from django.templates import RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Post
from django import forms


def darkmode(request):
    x = 'checked'
    return render(request, 'layout.html',{'input':x})


class RegisterView(FormView):
    template_name = 'index.html'
    form_class = UserCreationForm
    success_url = '/'


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post'
    ordering = ['-PostingDate']
    paginate_by = 10




def edithtml(request):
    return render(request, 'edit.html')


def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserRegister()
        messages.error(request, 'Registration error')

    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'register.html', {'user': form})


def login(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserLogin()
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html', {'form': form, })


def layout(request):
    form = UserLogin()
    dark = True
    return render(request, 'layout.html', {'dark': dark, 'user': form})


def logout(request):
    logoutuser(request)
    return redirect('/login')

class AddVideoView(CreateView):
    template_name = 'main/video_form.html'
    form_class = VideoForm
    success_url = '/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.authors_id = self.request.user.pk
        post.type = 'video'
        if 'https://www.youtube.com/watch?v=' == post.url[:32]:
            reUrl = post.url[32:43]
        elif 'https://youtu.be/' in post.url:
            reUrl = post.url[17:28]
        elif 'www.youtube.com' == post.url[:15]:
            reUrl = post.url[15:26]
        elif 'youtube.com' == post.url[:11]:
            reUrl = post.url[11:22]
        post.url = reUrl
        # article.save()  # This is redundant, see comments.
        return super(AddVideoView, self).form_valid(form)

class AddPostView(CreateView):
    template_name = 'main/post_form.html'
    form_class = ImageForm
    success_url = '/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.authors_id = self.request.user.pk
        post.type = 'img'
        # article.save()  # This is redundant, see comments.
        return super(AddPostView, self).form_valid(form)


class PostView(DetailView):
    model = Post

class VideoUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['heading', 'instagram']
    success_url = '/'
    template_name = 'video_update.html'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['heading', 'instagram', 'image']
    success_url = '/'
    template_name = 'post_update.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDel(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post_del.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'Users'
    ordering = ['-last_login']
    paginate_by = 10


class UserDetail(DetailView):
    model = User
    template_name = 'userDetail.html'
    context_object_name = 'User'

    def get_context_data(self, **kwargs):
        content = super(UserDetail, self).get_context_data(**kwargs)
        x = True
        if len(Post.objects.all()) == 0:
            x = False
        content.update({
            'Post': Post.objects.order_by('-pk').filter(author=self.kwargs['pk']),
            'len': x ,
        })
        return content


class Search(ListView):
    template_name = 'users.html'
    paginate_by = 10
    context_object_name = 'Users'


    def get_queryset(self):
        return User.objects.filter(username__icontains=self.request.GET.get('user'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = self.request.GET.get('user')
        return context

def add(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    return render(request, 'add.html')


# 404////////////////
def Page404(request):

    return render(request, '404.html')
