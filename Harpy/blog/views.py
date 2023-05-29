from typing import Optional
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post    # from models.py file in curr folder, import 'Post' class

def home(request):      # Function-based view for homepage
    return render(request, 'blog/home.html', {'posts':Post.objects.all()})

class PostListView(ListView):       # Class-based view for all the posts
    model = Post    # Use 'Post' model/table to construct this listview
    template_name = 'blog/home.html'    # Use this html file as the template, that is, don't follow the default naming convention <app>/<model>_<viewtype>.html
    context_object_name = 'posts'   # To avoid conflict between PostListView and home() view
    ordering = ['-date_posted']     # Order posts by latest

# When we look at a particular post, it is going to be a detailed view. Because we want to see all the description,date etc of that post.
class PostDetailView(DetailView):       # Class-based view for the details of all the posts
    model = Post    # Use 'Post' model/table to construct this view
    context_object_name = 'post'
    
# Class-based view for creating a new post
class PostCreateView(LoginRequiredMixin, CreateView):       # One has to be logged-in in order to post something
    model = Post    # Use 'Post' model/table to construct this view
    fields = ['title','content']
    
    # Author is set as the current logged-in user by overriding form_valid() function.
    def form_valid(self, form):
        form.instance.author = self.request.user    # modify the author attribute of this form instance
        return super().form_valid(form)             # then call the method of the parent containing this modified form 
    
# Class-based view for updating an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):       # One has to be logged-in in order to post something
    model = Post    # Use 'Post' model/table to construct this view
    fields = ['title','content']
    
    # Author is set as the current logged-in user by overriding form_valid() function.
    def form_valid(self, form):
        form.instance.author = self.request.user    # modify the author attribute of this form instance
        return super().form_valid(form)             # then call the method of the parent containing this modified form 

    # Overriding test_func()
    def test_func(self):
        post = self.get_object()    # returns current 'Post' object
        # Check if the current user is the author of the post, if not, prevent them from modifying it.
        return (self.request.user == post.author)
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):       # Class-based view for deleting any post
    model = Post    # Use 'Post' model/table to construct this view
    context_object_name = 'post'
    success_url = '/'   # Redirect to homepage after deleting the post
    
    # Overriding test_func()
    def test_func(self):
        post = self.get_object()    # returns current 'Post' object
        # Check if the current user is the author of the post, if not, prevent them from deleting it.
        return (self.request.user == post.author)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

