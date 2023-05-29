from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),    # Different convention for the view: <app>/<model>_form.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),    # Same convention for the view as PostCreateView
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), # Different convention for the view: <app>/<model>_confirm_delete.html
    path('about/', views.about, name='blog-about'),
]

"""
When using class-based view, we can't just pass the class name as an argument, we need to call as_view() method to actually convert it into
a listview. Also, by default, a class-based view looks for a template of the following naming convention when rendering the view:
    <app>/<model>_<viewtype>.html
e.g., blog/post_list.html

path('post/<int:pk>/',...) 
e.g., post/1/ means that we want to see the details of the post with id 1, which is the primary key for 'Post' table and is an int.
This allows us to grab that id from the url and use it in the PostDetailView class to get the 'Post' object.
"""
