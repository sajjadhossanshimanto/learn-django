from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Q
from django.contrib import messages

from tasks.models import Task
from tasks.forms import TaskModelForm, TaskDetailModelForm


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

def create_task(request):
    task_form = TaskModelForm()
    task_details = TaskDetailModelForm()
    
    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_details = TaskDetailModelForm(request.POST)

        if task_form.is_valid() and task_details.is_valid():
            task = task_form.save()
            
            task_details = task_details.save(commit=False)
            task_details.task = task
            task_details.save()

            messages.success(request, 'Task Created Sucessfully')

    context = {
        'task_form': task_form,
        'task_detail_form': task_details
    }
    return render(request, 'taskform.html', context)

def update_task(request, id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)
        
    if task.details:
        task_details = TaskDetailModelForm(instance=task.details)

    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailModelForm(
            request.POST, instance=task.details)

        if task_form.is_valid() and task_detail_form.is_valid():

            """ For Model Form Data """
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task Updated Successfully")

    context = {
        'task_form': task_form,
        'task_detail_form': task_details
    }
    return render(request, 'taskform.html', context)