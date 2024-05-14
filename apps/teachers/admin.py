from django.contrib import admin
from .models import *


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_classes_taught')

    def get_classes_taught(self, obj):
        return ", ".join([str(class_taught) for class_taught in obj.classes_taught.all()])
    get_classes_taught.short_description = 'Classes Taught'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'classteacher')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'day_of_week',
                    'start_time', 'end_time', 'teacher')


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'degree', 'field',
                    'institution', 'year_completed')


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'amount', 'month')


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'start_date', 'end_date', 'reason', 'status')


@admin.register(SchoolStaff)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'phone_number', 'address')

@admin.register(SchoolEvent)
class SchoolEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'organizer')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title', 'description', 'location', 'organizer__username')
    date_hierarchy = 'start_date'
    ordering = ('-start_date',)