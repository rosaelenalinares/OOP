from rest_framework import serializers
from .models import Category, Product, OrderItem, CartOrder, Profile, CustomUser
from . import models
from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer



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

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'phone_number'
    )

    model = CustomUser


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=30)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.phone_number = self.data.get('phone_number')
        user.save()
        return user