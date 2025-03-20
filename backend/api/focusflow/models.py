from django.db import models
import uuid
from datetime import date
from django.contrib.auth.models import User


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(max_length=255, default="project title")

    def __str__(self):
        return f"{self.title}"
    
    def get_tasks(self):
        tasks = Task.objects.filter(project=self)
        data = []
        for task in tasks:
            data.append(task.to_dict())
        return data
    
    def to_dict(self):
        return {
            "id": self.id, 
            "title": self.title,
            "tasks": self.get_tasks()
        }
    
class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(max_length=255, default="Task title")
    description = models.CharField(max_length=255, default="description")
    date = models.DateField(default=date.today)
    class StatusTypes(models.TextChoices):
        Completed = "Completed"
        Inprogress = "In Progress"
        New = "New"
    status = models.CharField(max_length=20,choices=StatusTypes.choices, default=StatusTypes.New)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return f"{self.title}"
    
    
    def to_dict(self):
        return {
            "id": self.id, 
            "title": self.title,
            "description:": self.description,
            "date": self.date,
            "status": self.status,
            "project": self.project.title
        }
    
class UserTask(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="tasks")
    task = models.ForeignKey(Task,on_delete=models.CASCADE, related_name="users")
    class PriorityTypes(models.TextChoices):
        P1 = "P1"
        P2 = "P2"
        P3 = "P3"
    priority = models.CharField(max_length=20,choices=PriorityTypes.choices, default=PriorityTypes.P3)
    assigned = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.task} Assigned to {self.user}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user,
            "task": self.task,
            "priority": self.priority,
            "assigned": self.assigned
        }




    
# class UserTask(models.Model):
#     Task = models.ForeignKey(Task,on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.user}"