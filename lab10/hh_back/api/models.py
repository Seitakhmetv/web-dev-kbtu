from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(default="", max_length=200)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

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
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.__str__()
        }