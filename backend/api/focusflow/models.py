from django.db import models
import uuid
from datetime import date


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(max_length=255, default="project title")

    def __str__(self):
        return f"{self.title}"
    
    def to_dict(self):
        return {
            "id": self.id, 
            "title": self.title
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
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    
    def to_dict(self):
        return {
            "id": self.id, 
            "title": self.title,
            "description:": self.description,
            "date": self.date,
            "status": self.status,
            "project": self.project.to_dict()
        }
    
# class UserTask(models.Model):
#     Task = models.ForeignKey(Task,on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.user}"