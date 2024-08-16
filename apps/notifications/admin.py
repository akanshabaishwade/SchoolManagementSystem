from apps.notifications.models import *
from django.contrib import admin




@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at', 'updated_at')
    list_filter = ('is_read', 'created_at', 'updated_at')
    search_fields = ('user__username', 'message')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

