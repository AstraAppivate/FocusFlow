from django.contrib import admin
from .models import Project, Task, UserTask


admin.site.register(Project)
admin.site.register(Task)
admin.site.register(UserTask)

