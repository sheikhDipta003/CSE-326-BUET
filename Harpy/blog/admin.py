from django.contrib import admin
# Registering my models so that they show up in the localhost/admin page.
from .models import Post    # first import the model, i.e. the 'Post' class from models.py in curr folder
admin.site.register(Post)   # then register this model in admin module


