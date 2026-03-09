from django.urls import path,include
from rest_framework import routers
from .views import CartViewSet, CartItemViewSet

router=routers.DefaultRouter()
router.register('cart', CartViewSet)
router.register('cartItems', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
