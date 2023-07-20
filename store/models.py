from django.db import models

class Product(models.Model):
    slug = models.CharField(max_length=120)
    title = models.CharField('Product Name', max_length=120)
    image = models.FileField()
    price = models.FloatField('Price')
    description = models.TextField(blank=True)
    availability = models.BooleanField()
    date = models.DateTimeField('Release Date')

    def __str__(self):
        return self.title   