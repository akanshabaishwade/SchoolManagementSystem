from apps.notifications.models import *
from rest_framework import serializers




class NotificationSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(source='created', read_only=True)
    
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'is_read', 'delivered', 'created_at']
