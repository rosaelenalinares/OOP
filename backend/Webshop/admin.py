from django.contrib import admin
from .models import Category, Product, OrderItem, Order, Profile

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Profile)