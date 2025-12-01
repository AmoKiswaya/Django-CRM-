from django.conf import settings
from django.db import models

# Create your models here.
# from contacs.models import Contact
User = settings.AUTH_USER_MODEL


class Event(models.Model):
    class EventType(models.TextChoices):
        CREATED = "created", "Create Event"
        VIEWED = "viewed", "View Event"

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Performed by user",
        related_name="myevents",
    )
    type = models.CharField(
        max_length=40, default=EventType.VIEWED, choices=EventType.choices
    )
    object_id = models.IntegerField(blank=True, default=-1)
    model_name = models.CharField(max_length=120, default="contacts.content")
    timestamp = models.DateTimeField(auto_now_add=True)
