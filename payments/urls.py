from django.urls import path
from .views import CreatePaymentView, PaymentStatusView, PaymentTestView

urlpatterns = [
    path('create/', CreatePaymentView.as_view(), name='create_payment'),
    path('status/', PaymentStatusView.as_view(), name='payment_status'),
    path('test/', PaymentTestView.as_view(), name='payment_test'),
]