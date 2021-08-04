from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name ='items', on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField()
    imageurl = models.ImageField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(default=True)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=5, default='S')

    class meta:
        ordering = ['date_created']

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



