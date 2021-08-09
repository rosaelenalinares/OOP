from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Category, Product, OrderItem, CartOrder, Profile
from .serializers import CategorySerializer, ProductSerializer, OrderItemSerializer, CartOrderSerializer, ProfileSerializer
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.http import HttpResponse, request
import stripe
from django.conf import settings
import random
import string
from datetime import date
import datetime
stripe.api_key = settings.STRIPE_SECRET_KEY




# Create your views here.

class ListCategory(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListProduct(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListOrderItem(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class =OrderItemSerializer

class ListCartOrder(viewsets.ModelViewSet):
    queryset = CartOrder.objects.all()
    serializer_class = CartOrderSerializer

class ListProfile(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ListProfile(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


@login_required
def my_profile(request):
    user = request.user
    my_user_profile = Profile.objects.filter(user).first()
    my_orders = CartOrder.objects.filter(is_ordered=True, owner=my_user_profile)
    context = {
        'my_orders': my_orders,
        'user': user
    }

    # return render(request, 'profile.html', context)



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
    # return render(request, 'product_list.html', context)



def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = CartOrder.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


@login_required()
def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    if product in request.user.profile.product.all():
        messages.info(request, 'You already own this product')
        # return redirect(reverse('product_list'))
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = CartOrder.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "Item added to cart")
    # return redirect(reverse('product_list'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    # return redirect(reverse('order_summary'))


def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[
        2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str
    
@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    # return render(request, 'order_summary.html', context)
