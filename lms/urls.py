from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonViewSet, SubscriptionView

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet, basename='lessons')

urlpatterns = [
    path('', include(router.urls)),
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
]
