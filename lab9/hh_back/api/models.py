from pyexpat import model
from django.db import models
from django.forms import FloatField

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="", max_length=200)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.__str__()
        }