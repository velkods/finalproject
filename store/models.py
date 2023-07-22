from django.db import models

class GoodsList(models.Model):
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    title = models.CharField('Product Name', max_length=120)
    image = models.ImageField(upload_to='static/products')
    price = models.FloatField('Price')
    description = models.TextField(blank=True)
    availability = models.BooleanField()
    date = models.DateTimeField('Release Date')

    def __str__(self):
        return self.title   