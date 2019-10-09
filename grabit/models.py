import email
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Item(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    is_worthy = models.BooleanField(default=None, blank=True, null=True)

    def __str__(self):
        return self.title

class User(AbstractUser):
    is_worthy = models.BooleanField(default=None, blank=True, null=True)


