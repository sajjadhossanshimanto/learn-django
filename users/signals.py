from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def send_activation_mail(sender, instance, created, **kwargs):
    if not created: return
    
    token = "1224345wlfjlzkdjfljs"
    activation_url = f'{settings.BASE_URL}/{instance.id}/{token}'
    message = f"Hi {instance.username}\n\nPlsease active your account by clicking the link bellow \n{activation_url}\n\nThank you"

    send_mail(
        subject="Activation mail",
        message=message,
        from_email=settings.EMAIL_SENDER,
        recipient_list=[instance.email]
    )
