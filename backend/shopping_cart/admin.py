from django.contrib import admin

from shopping_cart.models import CartOrderItem, CartOrder, Transaction

admin.site.register(CartOrderItem)
admin.site.register(CartOrder)
admin.site.register(Transaction)
