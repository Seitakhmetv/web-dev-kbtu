from itertools import product
from unicodedata import category, name
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=300)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
        }
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    description = models.TextField(max_length=1000)
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active,
            'category': self.category.__str__(),
        }
    
    def __str__(self):
        return self.name