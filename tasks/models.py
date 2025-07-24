from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'pending'),
        ('IN_PROGRESS', 'In progress'),
        ('COMPLETED', 'Completed')
    ]
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default="PENDING")
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        default=1
    )
    assigned_to = models.ManyToManyField(Employee, related_name='tasks')
    title = models.CharField(max_length=250)
    due_date = models.DateField()
    # is_completed = models.BooleanField(default=False)# status=completed does the same
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'task: {self.title}'

class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    )
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        related_name='details'
    )

    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_OPTIONS,
        default=LOW
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Details from Task {self.task.title}'

class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
    
