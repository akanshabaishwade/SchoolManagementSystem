from apps.notifications.api import *
from django.urls import path


urlpatterns = [
    #---------Notification---------
    path('notification/get/',NotificationGetApi.as_view(),name="Notification-get"),
    path('notification/post/',NotificationPostApi.as_view(),name="Notification-post"),
]
