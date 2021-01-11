from django.db import models

from datetime import datetime


class Product(models.Model):
    tittle = models.CharField(max_length=200)
    price = models.IntegerField()
    sale = models.IntegerField()
    category = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    vendor = models.CharField(max_length=200)
    made_in = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.tittle
