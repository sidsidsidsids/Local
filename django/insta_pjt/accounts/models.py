from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(null=True, max_length=40)
    introduction = models.TextField(null=True)
    image_f = models.ImageField(null=True)
    image_file = ImageSpecField(
                                source = 'image_f',
                                processors=[ResizeToFill(300,300)],
                                format='JPEG',
                                options={'quality':90}
                                )
    def __str__(self):
        return self.user.username
