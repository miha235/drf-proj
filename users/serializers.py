# users/serializers.py
from rest_framework import serializers
from .models import Payment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone", "city", "avatar"]  # Поле 'username' исключено, так как оно не используется
        extra_kwargs = {
            'password': {'write_only': True}  # Чтобы пароль не был включен в ответ
        }

class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для платежей."""
    class Meta:
        model = Payment
        fields = "__all__"

