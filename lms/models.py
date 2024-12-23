from django.contrib.auth import (
    get_user_model,
)  # Используем для работы с моделью пользователя
from django.db import models

User = "users.User"
# Получаем текущую модель пользователя


class Course(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    preview = models.ImageField(
        upload_to="course_previews/",
        blank=True,
        null=True,
        verbose_name="Картинка",
        help_text="Загрузите картинку",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Укажите описание курса"
    )

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "user",
            "course",
        )  # Уникальная подписка: один пользователь на один курс
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class Lesson(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Укажите описание урока"
    )
    preview = models.ImageField(
        upload_to="lesson_previews/",
        blank=True,
        null=True,
        verbose_name="Картинка",
        help_text="Загрузите картинку",
    )
    video_url = models.URLField()
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
