from django.contrib.auth import get_user_model
from django.test import TestCase
from lms.models import Course

class SubscriptionTestCase(TestCase):
    def setUp(self):
        # Создание пользователя с email, без username
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com", password="password"
        )
        # Создание курса
        self.course = Course.objects.create(name="Test Course")
        # Пример подписки пользователя на курс
        self.subscription = self.user.subscriptions.create(course=self.course)

    def test_create_subscription(self):
        # Проверка создания подписки
        self.assertEqual(self.subscription.user, self.user)
        self.assertEqual(self.subscription.course, self.course)

    def test_delete_subscription(self):
        # Проверка удаления подписки
        self.subscription.delete()
        with self.assertRaises(self.user.subscriptions.model.DoesNotExist):
            self.user.subscriptions.get(course=self.course)
