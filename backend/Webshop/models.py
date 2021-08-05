from django.db import models
from django.conf import settings

from django.db.models.signals import post_save

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


class Product(models.Model):
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
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
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


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    user_profile, created = Profile.objects.get_or_create(user=instance)

    if user_profile.stripe_id is None or user_profile.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email=instance.email)
        user_profile.stripe_id = new_stripe_id['id']
        user_profile.save()


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)



