
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    username = models.CharField(max_length=80, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email_n = models.EmailField(unique=True)
    membership_date = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Add a unique related_name
        blank=True,
        help_text="The groups this user belongs to.",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Add a unique related_name
        blank=True,
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return self.username
#Create your models here.
