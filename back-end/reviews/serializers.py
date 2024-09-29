from rest_framework import serializers
from .models import Restaurant, Dinner, Review

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number', 'website']

class DinnerSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Dinner
        fields = ['id', 'restaurant', 'name', 'description', 'price', 'date']

class ReviewSerializer(serializers.ModelSerializer):
    dinner = DinnerSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'dinner', 'user', 'rating', 'comment', 'date_posted']