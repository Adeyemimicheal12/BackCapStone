from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserCreateSerializer
from rest_framework import status,exceptions
from rest_framework.response import Response
# Create your views here.
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self,request):
        user = request.user
        serial_user = CustomUserCreateSerializer(user).data
        if request.user.is_authenticated:
            return Response(serial_user, status=status.HTTP_200_OK)
        else:
            return Response({"error": "unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)