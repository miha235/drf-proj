from rest_framework import serializers
from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для уроков."""
    class Meta:
        model = Lesson
        fields = "__all__"  # Включает все поля модели Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для курсов, включая уроки."""
    lessons = LessonSerializer(many=True, read_only=True)
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"  # Включает все поля модели Course

    def get_lesson_count(self, obj):
        """Возвращает количество уроков для курса."""
        return obj.lessons.count()  # Используем related_name "lessons"
