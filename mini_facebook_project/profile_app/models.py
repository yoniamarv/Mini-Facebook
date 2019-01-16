from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField()
  picture = models.ImageField(upload_to='profile_pictures', blank=True)
  follows = models.ManyToManyField('Profile', related_name='followed_by', symmetrical=False, blank=True)

  def __str__(self):
    return (self.user.username) + ' ' + str(self.id) 