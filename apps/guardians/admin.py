from django.contrib import admin
from .models import *

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('name', 'student', 'relationship_to_student', 'email', 'phone_number', 'occupation', 'address', 'address_link')

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'student', 'relationship_to_student', 'phone_number', 'alternate_phone_number')

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('student', 'guardian', 'teacher', 'datetime', 'complaint_type', 'status')
    list_filter = ('status', 'complaint_type')
    search_fields = ('student__name', 'guardian__name', 'teacher__name', 'description')

@admin.register(PTM)
class PTMAdmin(admin.ModelAdmin):
    list_display = ('guardian', 'student', 'teacher', 'datetime', 'location', 'status')
    list_filter = ('status',)
    search_fields = ('guardian__name', 'student__name', 'teacher__name', 'location', 'agenda', 'notes')
