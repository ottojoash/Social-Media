from rest_framework import viewsets
from .models import SocialMediaAccount, ScheduledPost
from .serializers import SocialMediaAccountSerializer, ScheduledPostSerializer

class SocialMediaAccountViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaAccount.objects.all()
    serializer_class = SocialMediaAccountSerializer

class ScheduledPostViewSet(viewsets.ModelViewSet):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer
