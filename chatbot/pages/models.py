from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Query(models.Model):
    query = models.TextField(null=False)
    reply = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(datetime.now(), null=True)
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.query
    
class Conversation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(datetime.now() ,null=True)