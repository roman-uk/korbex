from django.db import models


# >>>>>>>>> Models from Home Page <<<<<<<<<<<
#    Model for a record on the Home page
class HomeContent(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(help_text="input your text")
    image = models.ImageField(null=True, blank=True, upload_to='home_image')
    data_add = models.DateTimeField(auto_now=True, null=True, blank=True)

    # Overriding the save method so that when an image is deleted or updated,
    #           the old image is deleted from the storage
    def save(self, *args, **kwargs):
        if self.pk:
            old_record = HomeContent.objects.get(pk=self.pk)
            if old_record.image != self.image:
                old_record.image.delete(save=False)
        super(HomeContent, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    # adding an imageURL method to exclude an error if the image is missing
    @property
    def imageUrl(self):
        try:
            wg = self.image.url
        except:
            wg = ''
        return wg


# >>>>>>> Models from Store page <<<<<<<<
#     Model for a product on the Store page
class StoreProducts(models.Model):
    image = models.ImageField(null=True, blank=True, verbose_name='Obrazek do towaru', upload_to='store_image')
    name_product = models.CharField(max_length=40, unique=True, verbose_name='Nazwa towaru')
    incomplete_description = models.TextField(max_length=180, verbose_name='Krótki opis towaru')
    continue_description = models.TextField(null=True, blank=True, verbose_name='Pełny opis towaru')
    price = models.PositiveIntegerField(verbose_name='Cena towaru')

    def __str__(self):
        return self.name_product

    # Overriding the save method so that when an image is deleted or updated,
    #           the old image is deleted from the storage
    def save(self, *args, **kwargs):
        if self.pk:
            old_record = StoreProducts.objects.get(pk=self.pk)
            if old_record.image != self.image:
                old_record.image.delete(save=False)
        super(StoreProducts, self).save(*args, **kwargs)

    # adding an imageURL method to exclude an error if the image is missing
    @property
    def imageUrl(self):
        try:
            im = self.image.url
        except:
            im = ''
        return im


#  >>>>>>>>>* Models from Service page *<<<<<<<<<<<
#     Model for a type repair on the Service page
class TypeRepair(models.Model):
    type_repair = models.CharField(max_length=50, unique=True, help_text="Typ naprawy(kierownica, hamulca itp)")

    def __str__(self):
        return self.type_repair

# Model for a repair on the Service page
class Service(models.Model):
    name_repair = models.CharField(max_length=50, help_text="Nazwa naprawy(wymiana kierownicy)", unique=True)
    type_repair = models.ForeignKey(TypeRepair, on_delete=models.PROTECT)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.name_repair


# >>>>>>> Models from Blog page <<<<<<<<
# Model for a record on the blog page
class Blog(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Tytulł')
    content = models.TextField(verbose_name='Treść')
    image = models.ImageField(null=True, blank=True, verbose_name='Obrazek do artyklu', upload_to='blog_image')
    data_add = models.DateField(auto_now=True)
    author = models.CharField(max_length=20, verbose_name='Awtor artyklu')

    # Overriding the save method so that when an image is deleted or updated,
    #           the old image is deleted from the storage
    def save(self, *args, **kwargs):
        if self.pk:
            old_record = Blog.objects.get(pk=self.pk)
            if old_record.image != self.image:
                old_record.image.delete(save=False)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    # adding an imageURL method to exclude an error if the image is missing
    @property
    def imageUrl(self):
        try:
            wg = self.image.url
        except:
            wg = ''
        return wg


#   ==========Models from Contact page<<<<<<<<<<

# Model for a contact(address, telephone, facebook) on the Contact page
class ContactData(models.Model):
    address = models.TextField(max_length=200, blank=True)
    telephone = models.CharField(max_length=200, blank=True)
    facebook = models.URLField(verbose_name='facebook', blank=True)


# Model for a work day(and hour) on the Contact page
class WorkingHours(models.Model):
    week_day = (
        ('1.Poniedziałek', 'Poniedziałek'),
        ('2.Wtorek', 'Wtorek'),
        ('3.Środa', 'Środa'),
        ('4.Czwartek', 'Czwartek'),
        ('5.Piątek', 'Piątek'),
        ('6.Sobota', 'Sobota'),
        ('7.Niedzelia', 'Niedzelia'),
    )
    working_day = models.CharField(max_length=20, choices=week_day, verbose_name='Dzień tygodnia')
    working_hours = models.CharField(max_length=25, verbose_name='Godziny pracy')

    def __str__(self):
        return self.working_day
