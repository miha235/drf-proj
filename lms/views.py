from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Course, Lesson, Subscription
from .paginators import CustomPagination
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination  # Подключаем пагинацию


class LessonListCreateView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination  # Подключаем пагинацию


class LessonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def _get_course(self, course_id):
        """
        Извлекает курс по ID. Возвращает объект Course или Response с ошибкой.
        """
        if not course_id:
            return Response(
                {"error": "Не передан ID курса."}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response(
                {"error": "Курс не найден."}, status=status.HTTP_404_NOT_FOUND
            )

        return course

    def post(self, request):
        """
        Обработчик для создания подписки.
        """
        course_id = request.data.get("course_id")
        course = self._get_course(course_id)

        if isinstance(course, Response):  # Если вернулся Response с ошибкой
            return course

        # Логика создания подписки
        Subscription.objects.create(user=request.user, course=course)
        return Response(
            {"message": "Подписка успешно создана."}, status=status.HTTP_201_CREATED
        )

    def delete(self, request):
        """
        Обработчик для удаления подписки.
        """
        course_id = request.data.get("course_id")
        course = self._get_course(course_id)

        if isinstance(course, Response):  # Если вернулся Response с ошибкой
            return course

        # Логика удаления подписки
        try:
            subscription = Subscription.objects.get(user=request.user, course=course)
            subscription.delete()
            return Response(
                {"message": "Подписка успешно удалена."}, status=status.HTTP_200_OK
            )
        except Subscription.DoesNotExist:
            return Response(
                {"error": "Подписка не найдена."}, status=status.HTTP_404_NOT_FOUND
            )
