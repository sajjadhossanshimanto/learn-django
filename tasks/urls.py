from django.urls import path
from tasks.views import manager_dashboard, user_dashboard


urlpatterns = [
    path("manager_dashboard", manager_dashboard, name='manager_dashboard'),
    path("user_dashboard", user_dashboard),

    path('create-task/', create_task, name='create-task'),
]