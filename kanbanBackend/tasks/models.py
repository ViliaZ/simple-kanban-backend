from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    created_at = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=100, default='empty title')
    description = models.TextField(null=True, default='empty description')
    assigned_user = models.ForeignKey(User, related_name='tasks', blank=True, null=True, default=None, on_delete=models.CASCADE)
    urgency = models.IntegerField(null=True, default=1)
    
    #category = models.