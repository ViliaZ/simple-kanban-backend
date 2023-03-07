from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    assigned_user = UserSerializer()
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'created_at', 'urgency','assigned_user']
