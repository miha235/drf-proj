import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_stripe_product(product_data):
    product = stripe.Product.create(
        name=product_data['title'],
        description=product_data['description']
    )
    return product


def create_stripe_price(product_id, amount):
    price = stripe.Price.create(
        product=product_id,
        unit_amount=int(amount * 100),  # копейки умножаем на 100, чтобы получить деревянный
        currency='руб'
    )
    return price


def create_stripe_session(price_id, course_id):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price_id,
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'{settings.SITE_URL}/payment/success?course_id={course_id}',
        cancel_url=f'{settings.SITE_URL}/payment/cancel?course_id={course_id}',
    )
    return session


def retrieve_stripe_session(session_id):
    return stripe.checkout.Session.retrieve(session_id)