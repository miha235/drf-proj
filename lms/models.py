from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=200)
    preview = models.ImageField(upload_to='course_previews', null=True, blank=True)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    last_updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        # Обновляем last_updated только при изменении других полей
        if self.pk:
            orig = Course.objects.get(pk=self.pk)
            if orig.title != self.title or orig.description != self.description:
                self.last_updated = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preview = models.ImageField(upload_to='lesson_previews', null=True, blank=True)
    video_link = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons')

    objects = models.Manager()


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscriptions')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return f"{self.user.email} subscribed to {self.course.title}"