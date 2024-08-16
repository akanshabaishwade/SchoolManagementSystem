from rest_framework import serializers
from base_app.models import *


class CustomUserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields = '__all__'