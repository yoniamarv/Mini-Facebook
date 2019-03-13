from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures', blank=True)
    follows = models.ManyToManyField(
        'Profile', related_name='followed_by', symmetrical=False, blank=True)

    def __str__(self):
        return (self.user.username) + ' ' + str(self.id)


class Statut(models.Model):
    text = models.TextField(max_length=140)
    date = models.DateTimeField(default=datetime.now)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='status', default=0)
    picture = models.ImageField(upload_to='statut_pictures', blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField(max_length=140)
    date = models.DateTimeField(default=datetime.now)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='comments', default=0)
    statut = models.ForeignKey(
        Statut, on_delete=models.CASCADE, related_name='comments', default=0)
    picture = models.ImageField(upload_to='comment_pictures', blank=True)

    def __str__(self):
        return self.text
