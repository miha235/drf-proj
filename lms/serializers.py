from rest_framework import serializers
from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'  # Включает все поля модели Lesson


class CourseSerializer(serializers.ModelSerializer):
    # Добавляем связанные уроки (Lesson) в сериализатор курса
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'  # Включает все поля модели Course
