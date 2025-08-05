import os
import django
from faker import Faker
import random
from tasks.models import User, Project, Task, TaskDetail
from django.contrib.auth.models import Group

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')
django.setup()

# Function to populate the database


def populate_db():
    # Initialize Faker
    fake = Faker()

    # Create Projects
    projects = [Project.objects.create(
        name=fake.bs().capitalize(),
        description=fake.paragraph(),
        start_date=fake.date_this_year()
    ) for _ in range(5)]
    print(f"Created {len(projects)} projects.")

    # Create Employees
    user_role = Group.objects.filter(name="User").first()
    employees = []
    for _ in range(10):
        u = User.objects.create(
            username = fake.user_name(),
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email=fake.email(),
            is_active = True,
        )
        u.groups.add(user_role)
        employees.append(u)
    print(f"Created {len(employees)} employees.")

    # Create Tasks
    tasks = []
    for _ in range(20):
        task = Task.objects.create(
            project=random.choice(projects),
            title=fake.sentence(),
            # description=fake.paragraph(),
            due_date=fake.date_this_year(),
            status=random.choice(['PENDING', 'IN_PROGRESS', 'COMPLETED']),
            # is_completed=random.choice([True, False])
        )
        task.assigned_to.set(random.sample(employees, random.randint(1, 3)))
        tasks.append(task)
    print(f"Created {len(tasks)} tasks.")

    # Create Task Details
    for task in tasks:
        TaskDetail.objects.create(
            task=task,
            priority=random.choice(['H', 'M', 'L']),
            notes=fake.paragraph()
        )
    print("Populated TaskDetails for all tasks.")
    print("Database populated successfully!")