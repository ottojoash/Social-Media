from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import SocialMediaAccount, ScheduledPost
from .serializers import SocialMediaAccountSerializer, ScheduledPostSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password


class SocialMediaAccountViewSet(ModelViewSet):
    queryset = SocialMediaAccount.objects.all()
    serializer_class = SocialMediaAccountSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

class ScheduledPostViewSet(ModelViewSet):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer
    permission_classes = [IsAuthenticated]

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        # Validation checks
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        user = User.objects.create(
            username=username,
            password=make_password(password),  # Hash the password
            email=email
        )
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)