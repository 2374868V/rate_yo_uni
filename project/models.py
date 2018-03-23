from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserProfile(models.Model):
    user_name = models.OneToOneField(User)
    userSlug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.userSlug = slugify(self.user_name)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_name.username


class Bathroom(models.Model):
    name = models.CharField(unique=True, max_length=20)
    building = models.CharField(max_length=100)
    level = models.CharField(max_length=4)
    gender = models.CharField(max_length=8)
    rating = models.DecimalField(blank=True, default=0.00, decimal_places=2, max_digits=3)
    bathroomSlug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.bathroomSlug = slugify(self.name)
        super(Bathroom, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class BathroomImage(models.Model):
    bathroom = models.ForeignKey(Bathroom, related_name='images')
    image = models.ImageField(blank=True, upload_to='bathroom_images')


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)
    responseTo = models.ForeignKey('self', related_name='reply', blank=True)

    def __str__(self):
        return self.date + self.comment[0:2]


class BathroomInteraction(models.Model):
    user = models.ForeignKey(UserProfile)
    b = models.ForeignKey(Bathroom)
    rate = models.IntegerField(blank=True)
    comment = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return self.b.name
