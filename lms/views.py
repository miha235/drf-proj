from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Course, Lesson, Subscription
from .serializers import CourseSerializer, LessonSerializer
from .permissions import IsModerator, IsOwner, ReadOnlyForAll
from .paginators import MaterialsPaginator


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = MaterialsPaginator

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.IsAuthenticated & ~IsModerator]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwner | IsModerator]
        else:
            permission_classes = [ReadOnlyForAll | IsOwner | IsModerator]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = MaterialsPaginator

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.IsAuthenticated & ~IsModerator]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwner | IsModerator]
        else:
            permission_classes = [ReadOnlyForAll | IsOwner | IsModerator]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SubscriptionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course_id')
        course = get_object_or_404(Course, id=course_id)

        subscription, created = Subscription.objects.get_or_create(user=user, course=course)

        if created:
            message = 'Подписка добавлена'
        else:
            subscription.delete()
            message = 'Подписка удалена'

        return Response({"message": message}, status=status.HTTP_200_OK)
