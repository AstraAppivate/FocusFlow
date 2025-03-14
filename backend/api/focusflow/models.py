from django.db import models
import uuid

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(max_length=255, default="project title")

    def __str__(self):
        return f"{self.title}"
