# users/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import RegisterView  # Ваше представление для регистрации
from .views import PaymentViewSet

router = DefaultRouter()
router.register(
    r"payments", PaymentViewSet, basename="payment"
)  # Этот путь должен быть доступен

urlpatterns = [
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("", include(router.urls)),  # Включаем маршруты, зарегистрированные в роутере
    path("register/", RegisterView.as_view(), name="register"),  # Эндпоинт регистрации
]
