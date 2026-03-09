from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

router=routers.DefaultRouter()#(DefaultRouter())automatically generate URLs
router.register('users',UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]



