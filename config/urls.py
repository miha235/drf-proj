from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Функция для главной страницы
def home(request):
    return HttpResponse("Welcome to the API!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Главная страница
    path("api/", include("lms.urls")),  # Маршруты для приложения lms
    path("api/users/", include("users.urls")),  # Маршруты для приложения users

    # Эндпоинты для авторизации и регистрации
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
