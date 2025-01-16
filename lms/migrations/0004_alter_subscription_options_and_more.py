from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


def set_default_owner(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    # Здесь можно выбрать пользователя, например, первого в базе данных
    default_owner = User.objects.first()
    if default_owner:
        # Применение значения по умолчанию для поля `owner` в модели `lesson`
        lessons = apps.get_model('lms', 'Lesson')
        lessons.objects.filter(owner__isnull=True).update(owner=default_owner)


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0003_alter_lesson_title_subscription"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subscription",
            options={},
        ),
        migrations.RenameField(
            model_name="lesson",
            old_name="video_url",
            new_name="video_link",
        ),
        migrations.AddField(
            model_name="course",
            name="owner",
            field=models.ForeignKey(
                default=1,  # Это может быть ID вашего администратора
                on_delete=django.db.models.deletion.CASCADE,
                related_name="courses",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.RunPython(set_default_owner, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name="course",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="course",
            name="preview",
            field=models.ImageField(blank=True, null=True, upload_to="course_previews"),
        ),
        migrations.AlterField(
            model_name="course",
            name="title",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="preview",
            field=models.ImageField(blank=True, null=True, upload_to="lesson_previews"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="title",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscriptions",
                to="lms.course",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscriptions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
