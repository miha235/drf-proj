from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonListCreateView, LessonDetailView

router = DefaultRouter()
router.register(r"courses", CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("lessons/", LessonListCreateView.as_view(), name="lesson-list"),
    path("lessons/<int:pk>/", LessonDetailView.as_view(), name="lesson-detail"),
]
