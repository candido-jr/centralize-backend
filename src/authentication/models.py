from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        CUSTOMER = "customer", "Customer"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        unique_together = ("user", "role")

    def __str__(self):
        return self.user.username
