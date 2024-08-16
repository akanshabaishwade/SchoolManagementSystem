from base_app.models import *
from django.db import models




class Notification(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications', to_field='username')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message
