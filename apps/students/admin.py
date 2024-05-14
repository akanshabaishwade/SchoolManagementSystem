from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'gender', 'phone_number', 'date_of_enrollment')
    search_fields = ('name__first_name', 'name__last_name', 'phone_number')
    list_filter = ('gender', 'date_of_enrollment')
    readonly_fields = ('date_of_enrollment',)
    fieldsets = (
        (None, {
            'fields': ('name', 'date_of_birth', 'gender', 'phone_number')
        }),
        ('Enrollment Information', {
            'fields': ('date_of_enrollment',),
            'classes': ('collapse',),
        }),
    )   


@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_date', 'day', 'is_present')
    list_filter = ('is_present',)


@admin.register(StudentPerformance)
class StudentPerformanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks')


@admin.register(StudentFee)
class StudentFeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'paid_amount', 'due_amount', 'classname', 'classfee', 'paid_date', 'is_paid')
    list_filter = ('is_paid',)


@admin.register(StudentHealthRecord)
class StudentHealthRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'height', 'weight', 'blood_group')
    search_fields = ('student__name',)


@admin.register(StudentAchievement)
class StudentAchievementAdmin(admin.ModelAdmin):
    list_display = ('student', 'achievement_date', 'description')
    search_fields = ('student__name',)
