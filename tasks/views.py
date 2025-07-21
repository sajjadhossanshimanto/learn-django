from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task


# Create your views here.
def manager_dashboard(request):
    task = Task.objects.all()
    
    context = {
        'tasks': task,
        'total_task': task.count(),
        'completed_task': Task.objects.filter(is_completed=True).count(),
        'in_progress_task': Task.objects.filter(status='IN_PROGRESS').count(),
    }
    return render(request, "manager_dashboard.html", context=context)

def user_dashboard(request):
    return render(request, "user_dashboard.html")
