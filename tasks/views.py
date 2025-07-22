from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
from django.db.models import Count, Q


# Create your views here.
def manager_dashboard(request):
    task = Task.objects.select_related('details').prefetch_related("assigned_to").all()
    count = Task.objects.aggregate(
        total_task = Count('id'),
        completed_task = Count('id', filter=Q(is_completed=True)),
        in_progress_task = Count('id', filter=Q(status='IN_PROGRESS')),
    )

    context = {
        'tasks': task,
        'total_task': count['total_task'],
        'completed_task': count['completed_task'],
        'in_progress_task': count['in_progress_task'],
    }
    return render(request, "manager_dashboard.html", context=context)

def user_dashboard(request):
    return render(request, "user_dashboard.html")
