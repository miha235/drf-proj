# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserListView(APIView):
    def post(self, request):
        # Логика для создания пользователя
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        # Логика для получения списка пользователей
        users = []  # Это пример. В реальном приложении вы получите пользователей из базы данных
        return Response({"users": users}, status=status.HTTP_200_OK)
