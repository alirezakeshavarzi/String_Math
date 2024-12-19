from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    membership_date = models.DateTimeField(auto_now_add=True)

    # Avoid conflicts with the default `auth.User` relationships
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Unique related name
        blank=True,
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Unique related name
        blank=True,
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return self.email
