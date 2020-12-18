from django.db import models
from datetime import date


class HomeContent(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(help_text="input your text")
    image = models.ImageField(null=True, blank=True)
    # image = models.ImageField(null=True, blank=True, upload_to=)
    data_add = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def imageUrl(self):
        try:
            wg = self.image.url
        except:
            wg = ''
        return wg


class Blog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(help_text="input your text")
    image = models.ImageField(null=True, blank=True)
    data_add = models.DateField(auto_now=True)
    author = models.CharField(max_length=20, help_text="type your name")

    def __str__(self):
        return self.title

    @property
    def imageUrl(self):
        try:
            wg = self.image.url
        except:
            wg = ''
        return wg

    

