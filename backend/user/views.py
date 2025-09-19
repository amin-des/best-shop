from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer, UserDisplaySerializer
from rest_framework.permissions import AllowAny , IsAuthenticated

User = get_user_model()

class user_registration(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class user_display(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserDisplaySerializer
    
    def get_object(self):
        return self.request.user
