from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    pass

admin.site.register(Task, TaskAdmin)

