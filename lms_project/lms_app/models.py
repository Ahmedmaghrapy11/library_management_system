
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):

    bookStatus = [
        ('available', 'available'),
        ('sold', 'sold'),
        ('rented', 'rented'),
    ]

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100, null=True, blank=True)
    bookPhoto = models.ImageField(upload_to= 'photos', null=True,blank=True)
    authorPhoto = models.ImageField(upload_to= 'photos', null=True,blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)
    rentPricePerDay = models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)
    rentalPeriod = models.IntegerField(null=True, blank=True)
    totalRent = models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=bookStatus, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title