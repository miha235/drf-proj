from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса",
        help_text="Укажите название курса")
    preview = models.ImageField(upload_to="course_previews/", blank=True, null=True, verbose_name="Картинка",
        help_text="Загрузите картинку")
    description = models.TextField(verbose_name="Описание",
        help_text="Укажите описание курса")

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название урока",
        help_text="Укажите назыание урока")
    description = models.TextField(verbose_name="Описание",
        help_text="Укажите описание урока")
    preview = models.ImageField(upload_to="lesson_previews/", blank=True, null=True, verbose_name="Картинка",
        help_text="Загрузите картинку")
    video_url = models.URLField()
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
