from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Путь к настройкам Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Использование настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическая регистрация задач
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')