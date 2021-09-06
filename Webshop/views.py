from .models import Category, CustomUser, Product, OrderItem, CartOrder, Profile
from .serializers import CategorySerializer, ProductSerializer, OrderItemSerializer, CartOrderSerializer, CustomUserSerializer, ProfileSerializer
from rest_framework import viewsets


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

class ListUser(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ListProfile(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer