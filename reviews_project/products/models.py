from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    PRODUCTS_CHOISES = [('1', 'NEW'), ('2', 'REFURBISHED'), ('3', 'USED')]
    category = models.CharField(max_length=1, choices=PRODUCTS_CHOISES, default='1')
    description = models.CharField(max_length=600, blank=True, null=True)
    picture = models.ImageField(null=True, blank=True, upload_to='product_pics', verbose_name='pic')

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', related_name='reviews', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    RATING_RANGE = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    rating = models.CharField(max_length=1, choices=RATING_RANGE, default='1')
    moderated = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author, self.product

