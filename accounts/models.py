from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Professional_level(models.TextChoices):
    SENIOR = "sênior"
    PLENO = "pleno"
    JUNIOR = "júnior"
    DEFAULT = "Não informado"


class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=127, unique=True)
    professional_level = models.CharField(
        max_length=14,
        choices=Professional_level.choices,
        default=Professional_level.DEFAULT,
    )
    kind_of_work = models.CharField(max_length=50, default="Não informado")

    REQUIRED_FIELDS = [
        "email",
    ]
