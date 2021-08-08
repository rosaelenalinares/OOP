from rest_framework import serializers
from .models import Category, Product, OrderItem, CartOrder, Profile
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title'

        )
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'category',
            'price',
            'description',
            'stock',
            'imageurl',
            'status',
            'date_created',
            'quantity',
            'size',
        )

        model = Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'is_ordered',
            'product',
            'date_added',
            'date_ordered',
            'quantity',
        )

        model = OrderItem


class CartOrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'owner',
            'ref_code',
            'items',
            'start_date',
            'date_ordered',
            'is_ordered',
        )

        model = CartOrder

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'product',
            'stripe_id',
        )

        model = Profile