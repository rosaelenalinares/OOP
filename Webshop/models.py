from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
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

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, default=True)
    lastname = models.CharField(max_length=50, default=True)
    product = models.ManyToManyField(Product)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_profile_products(self):
        return self.product.all()


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    user_profile, created = Profile.objects.get_or_create(user=instance)

    if user_profile.stripe_id is None or user_profile.stripe_id == '':
        new_stripe_id = stripe.Customer.create(email=instance.email)
        user_profile.stripe_id = new_stripe_id['id']
        user_profile.save()


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)



class OrderItem(models.Model):
    is_ordered = models.BooleanField(default=False)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(auto_now=True, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.product.title)




class CartOrder(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    ref_code = models.CharField(max_length=15, default=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    date_ordered = models.DateTimeField(auto_now=True)
    is_ordered = models.BooleanField(default=False)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)




