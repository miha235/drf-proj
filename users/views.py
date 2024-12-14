# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from users.models import Payment
from users.serializers import PaymentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PaymentFilter
from django.contrib.auth import get_user_model


User = get_user_model()



class UserListView(APIView):
    def post(self, request):
        # Логика для создания пользователя
        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )

    def get(self, request):
        # Логика для получения списка пользователей
        users = (
            []
        )  # Это пример. В реальном приложении вы получите пользователей из базы данных
        return Response({"users": users}, status=status.HTTP_200_OK)



class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentFilter
    ordering_fields = ["date"]