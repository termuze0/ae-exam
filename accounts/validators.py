import re
from django.core.exceptions import ValidationError


def validate_aes_username(value):
    pattern = r'^aes/\d{5}/\d{2}$'
    if not re.match(pattern, value):
        raise ValidationError(
            'Username must be in format aes/#####/## (e.g., aes/12345/01)'
        )