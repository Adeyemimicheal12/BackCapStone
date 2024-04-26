# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models
# from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

# class CustomUser(AbstractUser):
#     username = models.CharField(max_length=180, unique=True)
#     email = models.EmailField(max_length=50,  unique=True)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ['username']

#     objects = CustomUserManager()

#     def _str_(self):
#         return self.email

# from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=180, unique=True)
    email = models.EmailField(max_length=50,  unique=True)

    class Meta:
        # Ensure the app_label is set to the app where CustomUser is defined
        app_label = 'userservice'

    # Specify unique related_name for groups relationship
    groups = models.ManyToManyField(
        Group,
        verbose_name='group',
        blank=True,
        related_name='custom_users_groups'  # Choose a related_name specific to your CustomUser model
    )

    # Specify unique related_name for user_permissions relationship
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user_permissions',
        blank=True,
        related_name='custom_users_permissions'  # Choose a related_name specific to your CustomUser model
    )
