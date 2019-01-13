from django.db import models
from django.contrib.auth.models import User

class Gender(models.Model):
  name = models.CharField(max_length=264, default='')

  def __str__(self):
    return self.name

class Picture(models.Model):
  picture = models.ImageField()

  def __str__(self):
    return str(self.picture)


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField()
  picture = models.ImageField(default='static/images/profile.jpg', upload_to='static/images/pictures/')
  gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, default=0)

  def __str__(self):
    return self.user.username
