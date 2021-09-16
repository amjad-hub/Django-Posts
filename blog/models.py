from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 100)
    date_posted = models.DateTimeField(default = timezone.now)

    def str(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    
    def get_success_url(self):
        return reverse('blog-home')

