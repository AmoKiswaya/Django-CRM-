from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    notes = models.TextField(blank=True, default="")
