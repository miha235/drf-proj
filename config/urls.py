from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Функция для главной страницы
def home(request):
    return HttpResponse("Welcome to the API!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("api/", include("lms.urls")),
    path("api/users/", include("users.urls")),
]