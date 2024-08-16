from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import CustomUserPostSerializer  
from apps.notifications.signals import create_notification



class CustomerPostApi(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CustomUserPostSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            notification = create_notification(customer.username, "Welcome to School management system")
            if notification:
                return Response({
                    'customer': serializer.data,
                    'message': 'Congratulations! You are New user',
                    'notification': True
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'customer': serializer.data,
                    'message': 'Congratulations! You are New user',
                    'notification': False
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

