from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=100, default="My Bio", blank=True)
    followers= models.ManyToManyField(User, related_name='follower', blank=True)
    timestamp =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

    def profiles_posts(self):
        return self.image_set.all()


    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    class Meta:
        ordering=('-timestamp',)

class Image(models.Model):
    profileimage = CloudinaryField('image')
    author= models.ForeignKey(Profile, on_delete=models.CASCADE)
    profile_name = models.TextField()
    image_caption = models.CharField(max_length= 100, blank=True)
    comments = models.CharField(max_length=30,blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    timestamp = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.profile_name

    def total_likes(self):
        return self.likes.count()
    
    def save_profileimage(self):
        self.save()
    
    def delete_profileimage(self):
        self.delete()
    
    def update_profileimage(self):
        self._do_update()
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    user_id= models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    profileimage_id=models.ForeignKey(Image,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id} :{self.comment}'

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow' 
    

