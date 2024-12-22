from rest_framework.exceptions import ValidationError
import re

def validate_link(value):
    """
    Проверяет, что ссылка указывает только на youtube.com.
    """
    pattern = r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.*$"
    if not re.match(pattern, value):
        raise ValidationError("Разрешены только ссылки на youtube.com.")
