from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserProfile(models.Model):
    user_name = models.OneToOneField(User,
                                    on_delete=models.CASCADE)
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


class BathroomInteraction(models.Model):
    user = models.ForeignKey(UserProfile,
                            on_delete=models.CASCADE)
    b = models.ForeignKey(Bathroom,
                         on_delete=models.CASCADE)
    rate = models.IntegerField(blank=True)
    comment = models.CharField(blank=True, max_length=1000)

    def __str__(self):
        return self.b.name
