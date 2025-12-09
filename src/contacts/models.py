from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.conf import settings

from events.models import Event

User = settings.AUTH_USER_MODEL


# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mycontacts")
    email = models.EmailField()
    notes = models.TextField(blank=True, default="")
    last_edited_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="my_contact_edits"
    )
    events = GenericRelation(Event)

    def get_absolute_url(self):
        return f"/contacts/{self.id}/"
