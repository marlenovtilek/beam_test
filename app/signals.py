from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import User

@receiver(post_save, sender=User)
def user_created_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        message = f"Новый пользователь {instance.username} был создан!"

        async_to_sync(channel_layer.group_send)(
            'user_notifications',
            {
                'type': 'user_notification',
                'message': message
            }
        )