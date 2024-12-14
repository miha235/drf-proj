# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import PaymentViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')  # Этот путь должен быть доступен

urlpatterns = [
    path("users/", views.UserListView.as_view(), name="user-list"),
    path('', include(router.urls)),  # Включаем маршруты, зарегистрированные в роутере
]