from rest_framework import serializers
from .models import Restaurant, Dinner, Review, Reviewer
from django.contrib.auth.models import User

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class DinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinner
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.CharField(source='reviewer.user.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'date_posted', 'dinner', 'reviewer_name']

class ReviewerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    class Meta:
        model = Reviewer
        fields = ['id', 'user']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user