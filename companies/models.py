from django.db import models
import uuid


class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=150, unique=True)
    opening_hours = models.CharField(max_length=5)
    description = models.CharField(max_length=150)

    sector = models.ForeignKey(
        "sectors.Sector",
        on_delete=models.CASCADE,
        related_name="companies",
    )
