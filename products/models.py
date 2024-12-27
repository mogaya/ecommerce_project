from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    category = models.CharField(max_length=50)
    image_url = models.URLField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name