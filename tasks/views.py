from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from tasks.models import Task
from tasks.forms import TaskModelForm, TaskDetailModelForm


# validation functions
def is_manager(user):
    return 1

def is_empoloye(user):
    return 1


# Create your views here.
@login_required(login_url='login')
@user_passes_test(is_manager, login_url='no-permission')
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

@login_required(login_url='login')
@user_passes_test(is_empoloye, login_url='no-permission')
def user_dashboard(request):
    return render(request, "user_dashboard.html")

@permission_required('add_task', login_url='no-permission')
def create_task(request):
    task_form = TaskModelForm()
    task_details = TaskDetailModelForm()
    
    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_details = TaskDetailModelForm(request.POST, request.FILES)

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

@permission_required('change_task', login_url='no-permission')
def update_task(request, id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)
        
    if task.details:
        task_details = TaskDetailModelForm(instance=task.details)

    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailModelForm(
            request.POST, request.FILES, instance=task.details)

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

@permission_required('delete_task')
def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()# del qury
        messages.success(request, 'Task Deleted Successfully')
        return redirect('manager_dashboard')
    else:
        messages.error(request, 'Something went wrong')
        return redirect('manager_dashboard')

@permission_required("tasks.view_task", login_url='no-permission')
def task_details(request, task_id):
    task = Task.objects.get(id=task_id)
    # print("printing", task.status)
    if request.method=="POST":
        selected_status = request.POST['task_status']
        task.status = selected_status
        task.save()

    return render(request, 'task_details.html', {"task": task})
