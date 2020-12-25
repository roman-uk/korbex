from django.db import models
from datetime import date


class HomeContent(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(help_text="input your text")
    image = models.ImageField(null=True, blank=True)
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
    author = models.CharField(max_length=20, help_text="Imie awtora tekstu")

    def __str__(self):
        return self.title

    @property
    def imageUrl(self):
        try:
            wg = self.image.url
        except:
            wg = ''
        return wg


class TypeRepair(models.Model):
    type_repair = models.CharField(max_length=50, help_text="Typ naprawy(kierownica, hamulca itp)")

    def __str__(self):
        return self.type_repair

    
class Service(models.Model):
    name_repair = models.CharField(max_length=50, help_text="Nazwa naprawy(wymiana kierownicy)", unique=True)
    type_repair = models.ForeignKey(TypeRepair, on_delete=models.SET_DEFAULT, default='other')
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.name_repair
