from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#one to one relationship
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
