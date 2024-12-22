from django.contrib.auth import get_user_model
from django.test import TestCase
from lms.models import Course, Lesson

class CourseAndLessonTests(TestCase):
    def setUp(self):
        # Создание пользователя с использованием email, без username
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='password123'
        )
        # Создание курса и урока для тестов
        self.course = Course.objects.create(name='Test Course')
        self.lesson = Lesson.objects.create(course=self.course, name='Test Lesson')

    def test_access_without_authentication(self):
        # Пример теста на доступ без аутентификации
        response = self.client.get('/some_protected_url/')
        self.assertEqual(response.status_code, 302)  # Проверка перенаправления

    def test_create_course_as_admin(self):
        # Пример теста на создание курса администратором
        self.client.login(email='testuser@example.com', password='password123')
        response = self.client.post('/create_course/', {'name': 'New Course'})
        self.assertEqual(response.status_code, 201)  # Проверка успешного создания курса

    def test_create_course_as_user(self):
        # Пример теста на создание курса обычным пользователем
        self.client.login(email='testuser@example.com', password='password123')
        response = self.client.post('/create_course/', {'name': 'New Course'})
        self.assertEqual(response.status_code, 403)  # Ожидаем отказ в доступе

    def test_create_lesson_as_admin(self):
        # Пример теста на создание урока администратором
        self.client.login(email='testuser@example.com', password='password123')
        response = self.client.post('/create_lesson/', {'course': self.course.id, 'name': 'New Lesson'})
        self.assertEqual(response.status_code, 201)

    def test_create_lesson_as_user(self):
        # Пример теста на создание урока обычным пользователем
        self.client.login(email='testuser@example.com', password='password123')
        response = self.client.post('/create_lesson/', {'course': self.course.id, 'name': 'New Lesson'})
        self.assertEqual(response.status_code, 403)  # Ожидаем отказ в доступе

    def test_subscribe_to_course(self):
        # Пример теста на подписку на курс
        self.client.login(email='testuser@example.com', password='password123')
        response = self.client.post(f'/subscribe/{self.course.id}/')
        self.assertEqual(response.status_code, 200)  # Проверка успешной подписки

    def test_subscribe_to_course_twice(self):
        # Пример теста на попытку подписки дважды
        self.client.login(email='testuser@example.com', password='password123')
        self.client.post(f'/subscribe/{self.course.id}/')
        response = self.client.post(f'/subscribe/{self.course.id}/')  # Повторная подписка
        self.assertEqual(response.status_code, 400)  # Проверка ошибки из-за дублирования подписки

    def test_unsubscribe_from_course(self):
        # Пример теста на отписку от курса
        self.client.login(email='testuser@example.com', password='password123')
        self.client.post(f'/subscribe/{self.course.id}/')  # Подписка
        response = self.client.post(f'/unsubscribe/{self.course.id}/')  # Отписка
        self.assertEqual(response.status_code, 200)

    def test_unsubscribe_from_course_not_subscribed(self):
        # Пример теста на отписку от курса, на который не подписан пользователь
        self.client.login(email='testuser@example.com', password='password123')
        response = self.client.post(f'/unsubscribe/{self.course.id}/')  # Попытка отписки без подписки
        self.assertEqual(response.status_code, 400)  # Ожидаем ошибку
