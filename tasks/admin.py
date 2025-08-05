from django.contrib import admin
from tasks.models import Task, TaskDetail
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskDetail)
# admin.site.register(User) # already registered
