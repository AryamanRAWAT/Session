from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Profiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    id_user = models.IntegerField(blank=False)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images', default='Blank_profile_icon.png')
    location = models.CharField(max_length=100, null=True)
    interests = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.user.username