from distutils.command.upload import upload
from turtle import title
from django.db import models





class Home(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to = "rasm/")




class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to = "rasm/")



