from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.name.first_name} {obj.name.last_name}"
    
    class Meta:
        model = Student
        fields = '__all__'

