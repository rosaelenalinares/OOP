from django.urls import path
from .views import ListCategory, DetailCategory, ListProduct, DetailProduct, ListOrderItem, DetailOrderItem, ListOrder, DetailOrder, my_profile
from . import views

urlpatterns = [
    path('categories', ListCategory.as_view(), name='category'),
    path('categories/<int:pk>', DetailCategory.as_view(), name='singlecategory'),
    path('product', ListProduct.as_view(), name='item'),
    path('product/<int:pk>', DetailProduct.as_view(), name='singleitem'),
    path('orderItem', ListOrderItem.as_view(), name='orderItem'),
    path('orderItem/<int:pk>', DetailOrderItem.as_view(), name='singleorderitem'),
    path('order', ListOrder.as_view(), name='order'),
    path('order/<int:pk>', DetailOrder.as_view(), name='singleorder'),
    path('profile', views.my_profile, name='myprofile')
]