from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class blog(models.Model):
    image =  models.ImageField(upload_to='images')
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={
            'id':self.id
        })
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    blog = models.ForeignKey('blog', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username