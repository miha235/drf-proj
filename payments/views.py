from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from lms.models import Course
from .models import Payment
from .services import create_stripe_product, create_stripe_price, create_stripe_session, retrieve_stripe_session
from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication


class CreatePaymentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Создаем тестовый продукт для демонстрации
        stripe_product = create_stripe_product({
            'title': 'Тестовый курс',
            'description': 'Описание тестового курса'
        })

        # Создаем цену для продукта
        stripe_price = create_stripe_price(stripe_product.id, 1000)  # 10.00 в центах

        # Создаем сессию оплаты
        stripe_session = create_stripe_session(stripe_price.id, 'test_course')

        # Создаем запись о платеже
        payment = Payment.objects.create(
            user=request.user,
            amount=10.00,
            stripe_session_id=stripe_session.id
        )

        return Response({
            'payment_id': payment.id,
            'stripe_session_id': stripe_session.id,
            'checkout_url': stripe_session.url
        }, status=status.HTTP_201_CREATED)


class PaymentStatusView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        payment_id = request.query_params.get('payment_id')
        payment = get_object_or_404(Payment, id=payment_id, user=request.user)

        stripe_session = retrieve_stripe_session(payment.stripe_session_id)
        payment.status = stripe_session.payment_status
        payment.save()

        return Response({
            'payment_id': payment.id,
            'status': payment.status
        })


class PaymentTestView(TemplateView):
    template_name = 'payment_test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context