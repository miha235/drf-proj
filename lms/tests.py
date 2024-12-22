from django.test import TestCase
from users.models import User
from .models import Course, Subscription

class SubscriptionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser@example.com", password="password")
        self.course = Course.objects.create(title="Test Course", description="Test Description")
        self.client.login(email="testuser@example.com", password="password")

    def test_create_subscription(self):
        response = self.client.post('/api/subscriptions/', {'course_id': self.course.id})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Subscription.objects.count(), 1)

    def test_delete_subscription(self):
        subscription = Subscription.objects.create(user=self.user, course=self.course)
        response = self.client.delete('/api/subscriptions/', {'course_id': self.course.id})
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Subscription.objects.count(), 0)
