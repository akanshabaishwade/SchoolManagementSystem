from rest_framework import serializers
from .models import *
from datetime import datetime




class GuardianSerializer(serializers.ModelSerializer):
    student_full_name = serializers.SerializerMethodField()

    def get_student_full_name(self, obj):
        return f"{obj.student.name.first_name} {obj.student.name.last_name}"
    class Meta:
        model = Guardian
        fields = '__all__'
