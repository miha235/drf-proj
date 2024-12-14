import django_filters
from .models import Payment

class PaymentFilter(django_filters.FilterSet):
    # Фильтрация по точному совпадению курса
    course = django_filters.NumberFilter(field_name='course', lookup_expr='exact')
    # Фильтрация по точному совпадению урока
    lesson = django_filters.NumberFilter(field_name='lesson', lookup_expr='exact')
    # Фильтрация по точному совпадению способа оплаты
    payment_method = django_filters.ChoiceFilter(choices=Payment.PAYMENT_METHODS, lookup_expr='exact')
    # Фильтрация по диапазону даты
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    # Возможность сортировки по дате (по возрастанию или убыванию)
    ordering = django_filters.OrderingFilter(
        fields=(
            ('date', 'date'),  # Сортировка по дате
        ),
        field_labels={
            'date': 'Дата платежа'
        }
    )

    class Meta:
        model = Payment
        fields = ['course', 'lesson', 'payment_method', 'date_from', 'date_to']
