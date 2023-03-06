
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, default='')
    assigned_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    urgency = models.IntegerField(null=True, default=1)