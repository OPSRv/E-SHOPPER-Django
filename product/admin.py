from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "tittle", "is_published", "image_show", "price", "sale", "description", "vendor")
    list_filter = ("price",)
    list_per_page = 300


    def image_show(self, obj):
        if obj.photo_main:
            return mark_safe("<img src='{}' width='60' />".format(obj.photo_main.url))
        return "None"

    image_show.__name__ = 'images'


admin.site.register(Product, ProductAdmin) 
