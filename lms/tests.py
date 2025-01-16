from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse
from .models import Course, Lesson, Subscription

User = get_user_model()


class LessonCRUDTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='12345')
        self.moderator = User.objects.create_user(email='moderator@example.com', password='12345')
        self.moderator.groups.create(name='moderators')
        self.course = Course.objects.create(title='Test Course', description='Test Description', owner=self.user)
        self.lesson = Lesson.objects.create(title='Test Lesson', description='Test Description',
                                            course=self.course, owner=self.user, video_link='https://youtube.com/watch?v=dQw4w9WgXcQ')

    def test_create_lesson(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('lessons-list')
        data = {
            'title': 'New Lesson',
            'description': 'New Description',
            'course': self.course.id,
            'video_link': 'https://youtube.com/watch?v=dQw4w9WgXcQ'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_lesson(self):
        url = reverse('lessons-detail', args=[self.lesson.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('lessons-detail', args=[self.lesson.id])
        data = {'title': 'Updated Lesson'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.get(id=self.lesson.id).title, 'Updated Lesson')

    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('lessons-detail', args=[self.lesson.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='12345')
        self.course = Course.objects.create(title='Test Course', description='Test Description', owner=self.user)

    def test_subscribe_to_course(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('subscribe')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_from_course(self):
        Subscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)
        url = reverse('subscribe')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())


class CourseCRUDTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='12345')
        self.course = Course.objects.create(title='Test Course', description='Test Description', owner=self.user)

    def test_create_course(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('course-list')
        data = {
            'title': 'New Course',
            'description': 'New Description'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_course(self):
        url = reverse('course-detail', args=[self.course.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_course(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('course-detail', args=[self.course.id])
        data = {'title': 'Updated Course'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.get(id=self.course.id).title, 'Updated Course')

    def test_delete_course(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('course-detail', args=[self.course.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
