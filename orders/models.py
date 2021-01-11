from django.db import models
from datetime import datetime

class Orders(models.Model):
    tittle = models.CharField(max_length=200)
    price = models.IntegerField()
    sale = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    quantity = models.IntegerField()
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.tittle