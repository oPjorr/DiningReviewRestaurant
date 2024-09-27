from django.shortcuts import render

from rest_framework import viewsets
from .models import Restaurant, Dinner, Review
from .serializers import RestaurantSerializer, DinnerSerializer, ReviewSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DinnerViewSet(viewsets.ModelViewSet):
    queryset = Dinner.objects.all()
    serializer_class = DinnerSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
