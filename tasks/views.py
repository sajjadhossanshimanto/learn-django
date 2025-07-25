from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
from django.db.models import Count, Q


# Create your views here.
def manager_dashboard(request):
    task_type = request.GET.get('type', 'all')
    base_query = Task.objects.select_related('details').prefetch_related("assigned_to")

    if task_type=='completed':
        task = base_query.filter(status='COMPLETED')
    elif task_type=='in-progess':
        task = base_query.filter(status='IN_PROGRESS')
    elif task_type=='todo':
        task = base_query.filter(status='PENDING')
    else:
        task = base_query.all()
    
    count = Task.objects.aggregate(
        total_task = Count('id'),
        completed_task = Count('id', filter=Q(status='COMPLETED')),
        in_progress_task = Count('id', filter=Q(status='IN_PROGRESS')),
        pending_task = Count('id', filter=Q(status='PENDING'))
    )

    context = {
        'tasks': task,
        'total_task': count['total_task'],
        'completed_task': count['completed_task'],
        'in_progress_task': count['in_progress_task'],
        'pending_task': count['pending_task']
    }
    return render(request, "manager_dashboard.html", context=context)

def user_dashboard(request):
    return render(request, "user_dashboard.html")
