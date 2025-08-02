from django.db.models.signals import post_save, pre_save, m2m_changed, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from tasks.models import Task


@receiver(m2m_changed, sender=Task.assigned_to.through, dispatch_uid="notify_task_to_employee")
def notify_employees(sender, instance, action, **kw):
    if action=='post_add':
        # print(instance.assigned_to.all())# unfortunately empty
        emails = [emp.email for emp in instance.assigned_to.all()]

        send_mail(
            subject='New task assigned',
            message=f'You have been assigned to the task: {instance.title}',
            from_email=settings.EMAIL_SENDER,
            recipient_list=emails,
            fail_silently=False
        )
