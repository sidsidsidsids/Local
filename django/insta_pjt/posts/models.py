from django.db import models

# Create your models here.
class POST(models.Model):
    content = models.TextField()
    imagecontent = models.ImageField(blank=True, null=True)