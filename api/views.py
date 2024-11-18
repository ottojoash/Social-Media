from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import SocialMediaAccount, ScheduledPost
from .serializers import SocialMediaAccountSerializer, ScheduledPostSerializer

class SocialMediaAccountViewSet(ModelViewSet):
    queryset = SocialMediaAccount.objects.all()
    serializer_class = SocialMediaAccountSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

class ScheduledPostViewSet(ModelViewSet):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer
    permission_classes = [IsAuthenticated]
