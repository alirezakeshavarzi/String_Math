from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email_n = models.EmailField(unique=True)
    #password = models.CharField(max_length=100)
    membership_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email_n
# Create your models here.
