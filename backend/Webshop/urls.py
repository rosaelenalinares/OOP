from django.urls import path
from Webshop import views
from .views import (
    # my_profile,
    product_list,
    add_to_cart,
    delete_from_cart,
    order_details,
)


app_name = 'Webshop'

urlpatterns = [
    # path('profile/', views.my_profile, name='my_profile'),
    # path('profile/<int:pk>', views.my_profile, name='profile'),
    # path('product_list', views.product_list, name='product_list'),
    # path('add-to-cart/<item_id>/', views.add_to_cart, name="add_to_cart"),
    # path('delete_from_cart/<item_id>/', views.delete_from_cart, name='delete_item'),
    # path('order_details', views.order_details, name='order_details'),
]