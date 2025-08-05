from django.urls import path
from tasks.views import manager_dashboard, user_dashboard, create_task, update_task, delete_task, task_details


urlpatterns = [
    path("manager_dashboard", manager_dashboard, name='manager_dashboard'),
    path("user_dashboard", user_dashboard),

    path('create/', create_task, name='create-task'),
    path('update/<int:id>/', update_task, name='update-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('task-details/<int:task_id>/', task_details, name='task-details'),
]