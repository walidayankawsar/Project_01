from django.db import models

# Create your models here.




class Clients(models.Model):
    Picture = models.ImageField(upload_to='images/')



class Work(models.Model):
    name = models.CharField(max_length=100)
    work_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=1000)
    github_link = models.URLField()
    website_link = models.URLField()


class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)


class Profile(models.Model):
    picture = models.ImageField(upload_to='images/', default='images/default.jpg')


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)


class Social(models.Model):
    facebook = models.CharField(max_length=200, blank=True, null=True)
    github_username = models.CharField(max_length=50, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)

