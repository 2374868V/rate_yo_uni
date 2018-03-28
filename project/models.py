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
    building = models.CharField(max_length=100)
    level = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    rating = models.DecimalField(blank=True, default=0.0, decimal_places=1, max_digits=2)
    details = models.TextField(max_length=1000)
    name = models.CharField(max_length=50)
    b_slug = models.SlugField(unique=True)

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

    class Meta:
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return self.rating.__str__()


class BathroomImages(models.Model):
    bathroom = models.ForeignKey(Bathroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='static/images/bathroom')

    def __str__(self):
        return self.name
