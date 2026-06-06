import re
from django.core.exceptions import ValidationError

def validate_aes_username(value):
    pattern = r'^aes/\d+/\d+$'
    if not re.match(pattern, value):
        raise ValidationError('Username must be in the format aes/12345/67')