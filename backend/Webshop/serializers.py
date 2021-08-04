from rest_framework import serializers
from .models import Category, Item, OrderItem, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title'

        )
        model = Category


class ItemSerializer(serializers.ModelSerializer):
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

        model = Item

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'ordered',
            'item',
            'quantity',
        )

        model = OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'items',
            'start_date',
            'ordered_date',
            'ordered',
        )

        model = Order