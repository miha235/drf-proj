from rest_framework import serializers
from .models import User, Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'phone', 'city', 'avatar']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'payment_date', 'course', 'lesson', 'amount', 'payment_method']


class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'payment_date', 'course', 'lesson', 'amount', 'payment_method']


class UserProfileSerializer(serializers.ModelSerializer):
    payment_history = PaymentHistorySerializer(many=True, read_only=True, source='payments')
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar', 'payment_history']