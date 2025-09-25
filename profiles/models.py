from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    followers = models.ManyToManyField('self', through='FollowRelation', symmetrical=False, related_name='followings')


    def __str__(self):
        return f"{self.user.username} {self.pk}"
    

class FollowRelation(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followed_by')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follows')
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.user.username} follows {self.following.user.username}"
    
