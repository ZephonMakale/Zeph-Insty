from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    profile_image = models.ImageField(upload_to='posts/')
    profile_name = models.TextField()
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image_caption = models.CharField(max_length= 100, blank=True)
    timestamp = models.DateTimeField(default= timezone.now)
    
    
