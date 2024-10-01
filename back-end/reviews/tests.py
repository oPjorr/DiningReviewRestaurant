from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Restaurant, Dinner, Reviewer, Review

class RestaurantModelTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            address="123 Test St",
            phone_number="1234567890",
            website="http://test.com"
        )

    def test_restaurant_creation(self):
        self.assertEqual(self.restaurant.name, "Test Restaurant")
        self.assertEqual(self.restaurant.address, "123 Test St")
        self.assertEqual(self.restaurant.phone_number, "1234567890")
        self.assertEqual(self.restaurant.website, "http://test.com")

class DinnerModelTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            address="123 Test St",
            phone_number="1234567890",
            website="http://test.com"
        )
        self.dinner = Dinner.objects.create(
            restaurant=self.restaurant,
            name="Test Dinner",
            description="Test Description",
            price=10.00,
            date="2024-09-30"
        )

    def test_dinner_creation(self):
        self.assertEqual(self.dinner.name, "Test Dinner")
        self.assertEqual(self.dinner.description, "Test Description")
        self.assertEqual(self.dinner.price, 10.00)
        self.assertEqual(self.dinner.date, "2024-09-30")
        self.assertEqual(self.dinner.restaurant.name, "Test Restaurant")

class ReviewerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.reviewer = Reviewer.objects.create(user=self.user)

    def test_reviewer_creation(self):
        self.assertEqual(self.reviewer.user.username, "testuser")

class ReviewModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.reviewer = Reviewer.objects.create(user=self.user)
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            address="123 Test St",
            phone_number="1234567890",
            website="http://test.com"
        )
        self.dinner = Dinner.objects.create(
            restaurant=self.restaurant,
            name="Test Dinner",
            description="Test Description",
            price=10.00,
            date="2024-09-30"
        )
        self.review = Review.objects.create(
            dinner=self.dinner,
            reviewer=self.reviewer,
            rating=5,
            comment="Great dinner!",
            date_posted="2024-09-30T12:00:00Z"
        )

    def test_review_creation(self):
        self.assertEqual(self.review.dinner.name, "Test Dinner")
        self.assertEqual(self.review.reviewer.user.username, "testuser")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Great dinner!")
