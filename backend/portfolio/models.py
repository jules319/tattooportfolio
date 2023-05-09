from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    profile_image = models.ImageField(upload_to='artists/', blank=True, null=True)


class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "About"


class Tattoo(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='tattoos/')
    created_date = models.DateField()

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    profile_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
