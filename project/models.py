from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userSlug = models.SlugField(unique=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def save(self, *args, **kwargs):
        self.userSlug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Bathroom(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('N', 'Neutral'),
        ('M', 'Male'),
    )
    name = models.CharField(blank=False, unique=True, max_length=50)
    building = models.CharField(max_length=100)
    level = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bSlug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.userSlug = slugify(self.name)
        super(Bathroom, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField(blank=False)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Rate(models.Model):
    rating = models.IntegerField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.rating.__str__()
