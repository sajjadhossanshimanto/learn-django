from django.urls import path
from tasks.views import (
    ManagerDashboardView, EmployeeDashboardView, CreateTaskView, ViewTaskView, UpdateTaskView, DeleteTaskView, TaskDetailsView, DashboardView,
    Greetings, HiGreetings, HiHowGreetings, CreateTask, ViewProject, TaskDetail, UpdateTask
)

urlpatterns = [
    path('manager-dashboard/', ManagerDashboardView.as_view(), name="manager-dashboard"),
    path('user-dashboard/', EmployeeDashboardView.as_view(), name='user-dashboard'),
    path('create-task/', CreateTaskView.as_view(), name='create-task'),
    path('view_task/', ViewTaskView.as_view(), name='view-task'),
    path('task/<int:task_id>/details/', TaskDetailsView.as_view(), name='task-details'),
    path('update-task/<int:id>/', UpdateTaskView.as_view(), name='update-task'),
    path('delete-task/<int:id>/', DeleteTaskView.as_view(), name='delete-task'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('greetings/', HiHowGreetings.as_view(greetings='Hi Good Day!'), name='greetings'),
    # Legacy/other CBVs for reference
    path('create-task-cbv/', CreateTask.as_view(), name='create-task-cbv'),
    path('view-task-list/', ViewProject.as_view(), name='view-task-list'),
    path('task-detail-cbv/<int:task_id>/', TaskDetail.as_view(), name='task-detail-cbv'),
    path('update-task-cbv/<int:id>/', UpdateTask.as_view(), name='update-task-cbv'),
]
