from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    # custom fields
    portfolio_site = models.URLField(blank=True)
    # uploaded images are gonna be saved in media/profile_pics
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
