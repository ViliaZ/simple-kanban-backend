from django.http import HttpResponse
from django.core import serializers
from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import TaskSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        task = Task.objects.create(title=self.request.POST.get('title', ""),
                                   description=self.request.POST.get(
                                       'description', ""),
                                   urgency=self.request.POST.get('urgency', 1),
                                   category=self.request.POST.get(
                                       'category', ""),
                                   assigned_user=self.request.user)
        serialized_obj = serializers.serialize('json', [task, ])
        return HttpResponse(serialized_obj, content_type='application/json')
