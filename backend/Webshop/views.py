from django.shortcuts import render
from rest_framework import generics
from .models import Category, Product, OrderItem, Order, Profile
from .serializers import CategorySerializer, ItemSerializer, OrderItemSerializer, OrderSerializer

from django.shortcuts import render, get_object_or_404
from shopping_cart.models import CartOrder

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ItemSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ItemSerializer

class ListOrderItem(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class =OrderItemSerializer

class DetailOrderItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class ListOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class =OrderSerializer

class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def my_profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = CartOrder.objects.filter(is_ordered=True, owner=my_user_profile)
    context = {
        'my_orders': my_orders
    }

    return render(request, "index.html", context)


@login_required
def product_list(request):
    object_list = Product.objects.all()
    filtered_orders = CartOrder.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }
    return render(request, "index.html", context)