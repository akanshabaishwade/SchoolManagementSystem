from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.notifications.serializers import *
from apps.notifications.serializers import *
from rest_framework.views import APIView
from apps.notifications.models import *
from django.shortcuts import render
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from dotenv import load_dotenv




#--------------Notification-------------
class NotificationGetApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        notifications = Notification.objects.all()

        status = request.query_params.get('status')
        if status == 'read':
            notifications = notifications.filter(is_read=True)
        elif status == 'unread':
            notifications = notifications.filter(is_read=False)

        sort_by = request.query_params.get('sort', '-created_at')
        notifications = notifications.order_by(sort_by)
        
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        notification_ids = request.data.get('notification_ids', [])
        
        if not notification_ids:
            return Response({"error": "No notification IDs provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        notifications = Notification.objects.filter(id__in=notification_ids)
        notifications.update(is_read=True)
        
        return Response({"message": "Notifications marked as read"}, status=status.HTTP_200_OK)
  

class NotificationPostApi(APIView):
    permission_classes = [AllowAny]
    Serializer = NotificationSerializer

    def post(self, request, format = None):
        serializer = self.Serializer(data= request.data)
        if serializer.is_valid():
            notification = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
