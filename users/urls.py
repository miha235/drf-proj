from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserCreateView, PaymentListView, UserProfileView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('users/<int:id>/', UserProfileView.as_view(), name='user-profile'),
]
