from django.shortcuts import render

# Create your views here.
def home(request):
    tasks = [
        "Learn Django",
        "Learn Git",
        "Build Portfolio",
    ]

    context={
        "tasks":tasks
    }
    return render(request,"tasks/home.html",context)