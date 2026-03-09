from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSets, OrderItemViewSets

router=routers.DefaultRouter()
router.register('orders', OrderViewSets)
router.register('orderItems', OrderItemViewSets)

urlpatterns = [
    path('', include(router.urls))
]
