from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomeUser(AbstractUser):
    email = models.EmailField(unique=True)
    # phone_number = models.PositiveBigIntegerField(unique=True)

