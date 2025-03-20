from django.shortcuts import render
from django.http import JsonResponse
from focusflow.models import Project
from focusflow.models import Task
from focusflow.models import UserTask
from focusflow.models import UserProject

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

def usertasksView (request):
    usertasks = UserTask.objects.all()
    print(usertasks)
    data = []
    for usertask in usertasks:
        data.append(usertask.to_dict())
    return JsonResponse({"UserTask": data})

def userprojectsView (request):
    userprojects = UserProject.objects.all()
    print(userprojects)
    data = []
    for userproject in userprojects:
        data.append(userproject.to_dict())
    return JsonResponse({"UserProject": data})
    