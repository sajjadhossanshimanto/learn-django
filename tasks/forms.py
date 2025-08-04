from django import forms
from tasks.models import Task, TaskDetail


# Django Form
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'assigned_to']
        widgets = {
            'due_date': forms.SelectDateWidget,
            'assigned_to': forms.CheckboxSelectMultiple
        }


class TaskDetailModelForm(forms.ModelForm):
    class Meta:
        model = TaskDetail
        fields = ['priority', 'notes']

