from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification
from base_app.models import *

@receiver(post_save, sender=Notification)
def notification_created(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user_{instance.user.id}_notifications",
            {
                'type': 'notification_message',
                'message': instance.message
            }
        )

def create_notification(username, message):
    try:
        user_instance = CustomUser.objects.get(username=username)
        notification = Notification.objects.create(user=user_instance, message=message)
        print(notification, 'created')
    except CustomUser.DoesNotExist:
        print(f"Error: User with username '{username}' does not exist.")
        return None
    except Exception as e:
        print(f"Error creating notification: {str(e)}")
        return None