from rest_framework import generics
from .models import Leave
from .serializers import LeaveSerializer

class LeaveList(generics.ListAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
