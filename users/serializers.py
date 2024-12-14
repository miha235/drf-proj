# users/serializers.py
from rest_framework import serializers
from .models import Payment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "date_of_birth"]


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для платежей."""
    class Meta:
        model = Payment
        fields = "__all__"

