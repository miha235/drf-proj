# Базовый образ с Python
FROM python:3.12-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt /app/

# Установка зависимостей Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копирование проекта
COPY . /app/

# Экспорт переменных окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# Запуск сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
