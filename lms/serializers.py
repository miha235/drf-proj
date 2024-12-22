from rest_framework import serializers
from .models import Course, Lesson, Subscription
from .validators import validate_link



class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для уроков."""

    link = serializers.URLField(validators=[validate_link])  # Привязка валидатора

    class Meta:
        model = Lesson
        fields = "__all__"  # Включает все поля модели Lesson

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для курсов, включая уроки."""
    lessons = LessonSerializer(many=True, read_only=True)
    lesson_count = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = "__all__"  # Включает все поля модели Course

    def get_lesson_count(self, obj):
        """Возвращает количество уроков для курса."""
        return obj.lessons.count()  # Используем related_name "lessons"

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False


