from rest_framework.viewsets import ModelViewSet
from .models import Subscription, Course
from .serializers import CourseSerializer, SubscriptionSerializer, LessonSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Lesson

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .paginators import CustomPagination



class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination # Подключаем пагинацию

class LessonListCreateView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination # Подключаем пагинацию


class LessonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]  # Только для аутентифицированных пользователей

    def post(self, request):
        """
        Создание подписки.
        """
        user = request.user
        course_id = request.data.get('course_id')

        # Проверка наличия course_id
        if not course_id:
            return Response({"error": "Не передан ID курса."}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка существования курса
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"error": "Курс не найден."}, status=status.HTTP_404_NOT_FOUND)

        # Проверка существующей подписки
        if Subscription.objects.filter(user=user, course=course).exists():
            return Response({"error": "Вы уже подписаны на этот курс."}, status=status.HTTP_400_BAD_REQUEST)

        # Создание подписки
        subscription = Subscription.objects.create(user=user, course=course)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        """
        Удаление подписки.
        """
        user = request.user
        course_id = request.data.get('course_id')

        # Проверка наличия course_id
        if not course_id:
            return Response({"error": "Не передан ID курса."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Проверка существующей подписки
            subscription = Subscription.objects.get(user=user, course_id=course_id)
            subscription.delete()
            return Response({"message": "Подписка удалена."}, status=status.HTTP_204_NO_CONTENT)
        except Subscription.DoesNotExist:
            return Response({"error": "Подписка не найдена."}, status=status.HTTP_404_NOT_FOUND)