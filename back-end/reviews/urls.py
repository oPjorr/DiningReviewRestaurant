from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, DinnerViewSet, ReviewViewSet, ReviewerViewSet, RegisterView, user_info

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'dinners', DinnerViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'reviewers', ReviewerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/user/', user_info, name='user_info'),
]
