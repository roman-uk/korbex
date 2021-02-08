from django.db import models


# >>>>>>>>> Models from Home Page <<<<<<<<<<<
class HomeContent(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(help_text="input your text")
    image = models.ImageField(null=True, blank=True, upload_to='home_image')
    data_add = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_record = HomeContent.objects.get(pk=self.pk)
            if old_record.image != self.image:
                old_record.image.delete(save=False)
        super(HomeContent, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def imageUrl(self):
        try:
            wg = self.image.url
        except:
            wg = ''
        return wg


# >>>>>>> Models from Store page <<<<<<<<
class StoreProducts(models.Model):
    image = models.ImageField(null=True, blank=True)
    name_product = models.CharField(max_length=40, unique=True)
    incomplete_description = models.TextField(max_length=130)
    continue_description = models.TextField(max_length=600, null=True, blank=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name_product

    @property
    def imageUrl(self):
        try:
            im = self.image.url
        except:
            im = ''
        return im


#  >>>>>>>>>* Models from Service page *<<<<<<<<<<<
#     Model for specifying the kind of repair
class TypeRepair(models.Model):
    type_repair = models.CharField(max_length=50, unique=True, help_text="Typ naprawy(kierownica, hamulca itp)")

    def __str__(self):
        return self.type_repair


class Service(models.Model):
    name_repair = models.CharField(max_length=50, help_text="Nazwa naprawy(wymiana kierownicy)", unique=True)
    type_repair = models.ForeignKey(TypeRepair, on_delete=models.PROTECT)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.name_repair


# >>>>>>> Models from Blog page <<<<<<<<
class Blog(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Tytulł')
    content = models.TextField(verbose_name='Treść')
    image = models.ImageField(null=True, blank=True, verbose_name='Obrazek do artyklu', upload_to='blog_image')
    data_add = models.DateField(auto_now=True)
    author = models.CharField(max_length=20, verbose_name='Awtor artyklu')

    def save(self, *args, **kwargs):
        if self.pk:
            old_record = Blog.objects.get(pk=self.pk)
            if old_record.image != self.image:
                old_record.image.delete(save=False)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def imageUrl(self):
        try:
            wg = self.image.url
        except:
            wg = ''
        return wg


#   ***Models from Contact page***
class ContactData(models.Model):
    address = models.TextField(max_length=200, blank=True)
    telephone = models.TextField(max_length=200, blank=True)
    facebook = models.URLField(verbose_name='facebook', blank=True)


class WorkingHours(models.Model):
    working_day = models.CharField(max_length=20)
    working_hours = models.CharField(max_length=25)

    def __str__(self):
        return self.working_day
