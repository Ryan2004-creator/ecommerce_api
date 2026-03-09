from django.urls import path, include
from .views import ProductViewSets, CategoryViewSets
from rest_framework import routers

router= routers.DefaultRouter()
router.register('products', ProductViewSets)
router.register('category', CategoryViewSets)

urlpatterns = [
    path('', include(router.urls))
]
