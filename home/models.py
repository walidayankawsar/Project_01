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



