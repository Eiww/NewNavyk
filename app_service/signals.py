from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from NewNavyk import settings
from .models import Application


@receiver(post_save, sender=Application)
def send_application_notification(sender, instance, created, **kwargs):
    if created:
        subject = f'Новая заявка: {instance.program.title}'
        message = f'''
        Новая заявка:

        Имя: {instance.full_name}
        Телефон: {instance.phone}
        Email: {instance.email}
        Программа: {instance.program.title}
        Дата: {instance.created_at}
        '''

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['niktonikakoj0@gmail.com'],
            fail_silently=False,
        )
