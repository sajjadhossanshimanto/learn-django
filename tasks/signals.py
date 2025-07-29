from django.db.models.signals import post_save, pre_save, m2m_changed, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail

from tasks.models import Task


@receiver(post_save, sender=Task, dispatch_uid="notify_task_to_employee")
def notify_employees(sender, instance, created, raw, **kw):
    if created:
        print(instance)
        print(instance.assigned_to.all())# unfortunately empty
