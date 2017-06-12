from __future__ import unicode_literals

from django.db import models
from sevalinks.models import User
from contacts.manager import ContactsManager
# Create your models here.

STATUS_CODE = {0:"Pending",
               1:"Accepted",
               2:"Declined",
               3:"Blocked",
               4:"Received"}

class Contacts(models.Model):
    user_one_id = models.IntegerField()
    user_two_id = models.IntegerField()
    status = models.IntegerField()
    user_action_id = models.IntegerField()
    contact_status_created = models.DateTimeField(auto_now=True)

    #objects = ContactsManager()

    # class Meta:
    #     unique_together = [("user_one_id", "user_two_id")]
