from django.db import models
from django.conf import settings

# Create your models here.
class POST(models.Model):
    content = models.TextField()
    imagecontent = models.ImageField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(POST, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)