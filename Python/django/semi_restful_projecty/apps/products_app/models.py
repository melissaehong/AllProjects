from __future__ import unicode_literals
from django.utils.timezone import now
from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def update(self, id, form_info):
        product = Product.objects.get(id=id)
        product.name = form_info['name']
        product.description = form_info['description']
        product.price = form_info['price']
        product.save()

class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
