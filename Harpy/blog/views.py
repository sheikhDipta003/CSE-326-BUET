from django.shortcuts import render
from .models import Post    # from models.py file in curr folder, import 'Post' class

# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
