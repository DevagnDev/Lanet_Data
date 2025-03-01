from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Unique reverse accessor
        blank=True,
        help_text="The groups this user belongs to.",
        related_query_name="user"
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Unique reverse accessor
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user"
    )

    