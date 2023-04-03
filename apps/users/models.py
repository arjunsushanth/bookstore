from django.db import models
from django.contrib.auth.models import AbstractUser

# python manage.py migrate admin zero
# python manage.py migrate auth zero
# python manage.py migrate contenttypes zero
# python manage.py migrate sessions zero

class User(AbstractUser):
    pseudonym = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)