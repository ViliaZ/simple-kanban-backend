from rest_framework import viewsets
#from rest_framework import permissions
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    #permission_classes = [permissions.IsAuthenticated]

