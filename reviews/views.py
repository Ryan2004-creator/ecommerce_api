from django.shortcuts import render
from .models import Reviews
from .serializers import ReviewSerializer
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ReviewsViewset(viewsets.ModelViewSet):
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]#controls who can do what when interacting with the api endpoint. In this case, it allows authenticated users to perform any action (like creating, updating, or deleting reviews), while unauthenticated users can only read the reviews.

