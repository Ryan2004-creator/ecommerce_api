from django.urls import path, include
from .views import ReviewsViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('reviews', ReviewsViewset)

urlpatterns = [
    path('', include(router.urls))
]
