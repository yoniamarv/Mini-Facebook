from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(max_length=400, default=0)
  picture = models.ImageField(upload_to='static/images/profile_pictures/', blank=True)
  gender = models.CharField(max_length=264, default=0)
  # follows = models.ManyToManyField('UserProfileInfo', related_name='followed_by', symmetrical=)

  def __str__(self):
    return self.user.username
