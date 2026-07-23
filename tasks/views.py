from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    tasks=Task.objects.all() #ORM QUERY 
                             #A QuerySet is a collection of model objects returned by an ORM query.
                             #<QuerySet [Task, Task, Task]>
    context={
        "tasks":tasks     #"The context dictionary is used to pass data from the view to the template. Each key in the dictionary becomes a variable that the template can access and display."
    }
    return render(request,"tasks/home.html",context)