from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Course, Subscription, Lesson
from django.db import IntegrityError


User = get_user_model()

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Test Course",
            description="Test description for the course.",
        )

    def test_course_str(self):
        """Проверка, что метод __str__ возвращает правильное название курса"""
        self.assertEqual(str(self.course), "Test Course")

    def test_course_creation(self):
        """Проверка создания курса"""
        course = Course.objects.get(title="Test Course")
        self.assertEqual(course.description, "Test description for the course.")

from django.contrib.auth import get_user_model

class SubscriptionModelTest(TestCase):
    def setUp(self):
        # Создаем пользователя и устанавливаем пароль
        self.user = User.objects.create(username="testuser", email="testuser@example.com")
        self.user.set_password("password")
        self.user.save()

        # Логиним пользователя через force_login
        self.client.force_login(self.user)

        self.course = Course.objects.create(
            title="Test Course",
            description="Test description for the course.",
        )
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)

    def test_subscription_creation(self):
        """Проверка создания подписки"""
        subscription = Subscription.objects.get(user=self.user, course=self.course)
        self.assertEqual(subscription.user.username, "testuser")
        self.assertEqual(subscription.course.title, "Test Course")

    def test_unique_subscription(self):
        """Проверка, что подписка уникальна для одного пользователя и курса"""
        with self.assertRaises(IntegrityError):
            Subscription.objects.create(user=self.user, course=self.course)

class LessonModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Test Course",
            description="Test description for the course.",
        )
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            description="Test description for the lesson.",
            video_url="http://example.com/video",
            course=self.course,
        )

    def test_lesson_creation(self):
        """Проверка создания урока"""
        lesson = Lesson.objects.get(title="Test Lesson")
        self.assertEqual(lesson.description, "Test description for the lesson.")
        self.assertEqual(lesson.course.title, "Test Course")

    def test_lesson_str(self):
        """Проверка, что метод __str__ возвращает правильное название урока"""
        self.assertEqual(str(self.lesson), "Test Lesson")
