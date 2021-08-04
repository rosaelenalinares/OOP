from django.urls import path
from .views import ListCategory, DetailCategory, ListItem, DetailItem, ListOrderItem, DetailOrderItem, ListOrder, DetailOrder

urlpatterns = [
    path('categories', ListCategory.as_view(), name='category'),
    path('categories/<int:pk>', DetailCategory.as_view(), name='singlecategory'),
    path('item', ListItem.as_view(), name='item'),
    path('item/<int:pk>', DetailItem.as_view(), name='singleitem'),
    path('orderItem', ListOrderItem.as_view(), name='orderItem'),
    path('orderItem/<int:pk>', DetailOrderItem.as_view(), name='singleorderitem'),
    path('order', ListOrder.as_view(), name='order'),
    path('order/<int:pk>', DetailOrder.as_view(), name='singleorder'),
]