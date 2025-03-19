from django.shortcuts import render
from django.http import JsonResponse
from focusflow.models import Project
from focusflow.models import Task

# Create your views here.
def projectsView (request):
    projects = Project.objects.all()
    print(projects)
    data = []
    for project in projects:
        data.append(project.to_dict())
    return JsonResponse({"Projects": data})

def tasksView (request):
    tasks = Task.objects.all()
    print(tasks)
    data = []
    for task in tasks:
        data.append(task.to_dict())
    return JsonResponse({"Tasks": data})