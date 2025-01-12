from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CourseViewSet,
    LessonDetailView,
    LessonListCreateView,
    SubscriptionView,
)

router = DefaultRouter()
router.register(r"courses", CourseViewSet)
router.register(r'lessons', LessonViewSet, basename='lessons')

urlpatterns = [
    path("", include(router.urls)),
    path("lessons/", LessonListCreateView.as_view(), name="lesson-list"),
    path("lessons/<int:pk>/", LessonDetailView.as_view(), name="lesson-detail"),
    path("subscriptions/", SubscriptionView.as_view(), name="subscriptions"),
]

