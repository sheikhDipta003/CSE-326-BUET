from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    # 'reverse()' returns the absolute url (as a string) that the user is redirected to after creating a post.
    # PostCreateView then handles the view. Here, we want to be redirected to the details page.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    