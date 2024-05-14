from rest_framework import serializers
from .models import *
from datetime import datetime


class LeaveSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.teacher.user.first_name} {obj.teacher.user.last_name}"

    class Meta:
        model = Leave
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    class Meta:
        model = Teacher
        fields = '__all__'




class SchoolStaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolStaff
        fields = '__all__'