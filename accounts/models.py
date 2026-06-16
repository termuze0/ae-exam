from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.validators import validate_aes_username


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20,
        unique=True,
        validators=[validate_aes_username]
    )
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'accounts_customuser'

    def __str__(self):
        return self.username