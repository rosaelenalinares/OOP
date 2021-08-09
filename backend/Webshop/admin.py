from django.contrib import admin
from .models import Category, Product, OrderItem, CartOrder, Profile

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(CartOrder)
admin.site.register(Profile)