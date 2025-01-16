from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from urllib.parse import urlparse


def validate_youtube_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except ValidationError:
        raise ValidationError('Введите корректный URL.')

    domain = urlparse(value).netloc
    if domain != 'youtube.com' and domain != 'www.youtube.com':
        raise ValidationError('Разрешены только ссылки на youtube.com')